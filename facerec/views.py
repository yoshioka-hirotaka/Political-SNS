from django.http import HttpResponse
from django.shortcuts import render, redirect
import face_recognition

from .models import Face
from .forms import FaceForm

def index(request):
    return render(request, "facerec/index.html")

def facerec(request):
    return render(request, "facerec/facerec.html")

def shoot(request):
    return render(request, "facerec/shoot.html")

def upload(request):
    if request.method == "POST":
        face = Face.objects.get(user_name="ikeda")
        form = FaceForm(request.POST, request.FILES, instance=face)
        if form.is_valid():
            form.save()
            return redirect('facerec')
    else:
        form = FaceForm()

    context = {'form':form}
    return render(request, "facerec/upload.html", context)

def reco(request):
    face = Face.objects.filter(user_name="ikeda")

    # 学習させたい（登録したい）顔画像のファイル名をリストに格納
    train_img_name = face[0].face_img_train
    # 学習させた画像に対して、認証できるかテストに使う顔画像のファイル名をリストに格納
    test_img_name = face[0].face_img_test
    
    ### テストデータ ###
    # テストデータ（認証する人の顔画像）を読み込む
    test_img = face_recognition.load_image_file(test_img_name)
    
    # テストデータの顔画像から顔の領域のみを検出する
    test_img_location = face_recognition.face_locations(test_img, model="hog")
    assert len(test_img_location) == 1, "画像から顔の検出に失敗したか、2人以上の顔が検出されました"
    
    # テストデータの特徴量を抽出する
    (test_img_encoding, ) = face_recognition.face_encodings(test_img, test_img_location)
    
    ### 学習データ ###
    # 学習データの顔画像を読み込む
    train_img = face_recognition.load_image_file(train_img_name)
    
    # 学習データの顔画像から顔の領域のみを検出する
    # modelはhogとcnnを指定でき、cnnは重いが精度良い、hogは軽量だが精度は普通
    train_img_location = face_recognition.face_locations(train_img, model="hog")
    # 顔検出に失敗するとtrain_img_locationの長さは1となる
    # 顔検出に成功すると顔を検出し四角形で囲んだ四隅の座標を取得できる
    assert len(train_img_location) == 1, "画像から顔の検出に失敗したか、2人以上の顔が検出されました"
    
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
        return render(request, "facerec/reco.html", {"answer": answer})
    else:
        return render(request, "facerec/reco.html", {"answer": answer})