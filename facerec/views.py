from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import face_recognition
from django.views.decorators import gzip
from django.views.decorators.clickjacking import xframe_options_exempt
import cv2

from .models import Face
from .forms import FaceForm
from polls.models import Election

def index(request):
    return render(request, "facerec/index.html")

def facerec(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    return render(request, "facerec/facerec.html", {"election": election})

def gen(camera):
    while True:
        success, image = camera.read()
        
        # カメラからの読み取りが成功したかどうかを確認
        if not success:
            print("Failed to read from camera.")
            break

        # 画像が空でないか確認
        if image is None or image.size == 0:
            print("Received an empty frame!")
            continue

        ret, jpeg = cv2.imencode('.jpg', image)

        # エンコードが成功したかどうかを確認
        if not ret:
            print("Failed to encode image.")
            continue

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

@ gzip.gzip_page
@ xframe_options_exempt
def capture(request, election_id):
    return StreamingHttpResponse(gen(cv2.VideoCapture(1,cv2.CAP_DSHOW)),content_type='multipart/x-mixed-replace; boundary=frame')

def shoot(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    return render(request, "facerec/shoot.html", {"election": election})

def upload(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
    ret, frame = cap.read()
    cv2.imwrite("./media/face_images/test/test.jpg", frame)
    face_img_test = "./face_images/test/test.jpg"
    face = get_object_or_404(Face, user_name=request.user.id)
    face.face_img_test = face_img_test
    face.save()
    return render(request, "facerec/upload.html", {"election": election})

def reco(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    face = Face.objects.filter(user_name=request.user.id)

    # 学習させたい（登録したい）顔画像のファイル名をリストに格納
    train_img_name = face[0].face_img_train
    # 学習させた画像に対して、認証できるかテストに使う顔画像のファイル名をリストに格納
    test_img_name = face[0].face_img_test
    print(test_img_name)
    
    ### テストデータ ###
    # テストデータ（認証する人の顔画像）を読み込む
    test_img = face_recognition.load_image_file(test_img_name)
    
    # テストデータの顔画像から顔の領域のみを検出する
    # 顔検出に失敗するとtest_img_locationの長さは1となる
    # 顔検出に成功すると顔を検出し四角形で囲んだ四隅の座標を取得できる
    test_img_location = face_recognition.face_locations(test_img, model="hog")
    if len(test_img_location[0]) == 1:
        answer = "テストデータ顔認証失敗"
        return render(request, "facerec/fail.html", {"answer": answer, "election": election})
    
    # テストデータの特徴量を抽出する
    (test_img_encoding, ) = face_recognition.face_encodings(test_img, test_img_location)
    
    ### 学習データ ###
    # 学習データの顔画像を読み込む
    train_img = face_recognition.load_image_file(train_img_name)
    
    # 学習データの顔画像から顔の領域のみを検出する
    # modelはhogとcnnを指定でき、cnnは重いが精度良い、hogは軽量だが精度は普通
    train_img_location = face_recognition.face_locations(train_img, model="hog")
    if len(train_img_location[0]) == 1:
        answer = "学習データ顔認証失敗"
        return render(request, "facerec/fail.html", {"answer": answer, "election": election})

    # 学習データの特徴量を抽出する
    train_img_encoding = face_recognition.face_encodings(train_img, train_img_location)

    ### 判定 ###
    # 学習データとテストデータの特徴量を比較し、ユークリッド距離を取得する
    # 距離を見ることで顔がどれだけ似ているかわかる
    dists = face_recognition.face_distance(train_img_encoding, test_img_encoding)

    # 学習データとテストデータの距離が0.40以下のとき、顔が一致と判定
    answer = "失敗"
    for dist in dists:
        if dist < 0.40:
            answer = "成功"

    answer = "顔認証" + answer
    
    if answer == "顔認証成功":
        return render(request, "facerec/reco.html", {"answer": answer, "election": election})
    else:
        return render(request, "facerec/fail.html", {"answer": answer, "election": election})