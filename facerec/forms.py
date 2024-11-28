from django import forms
from .models import Face

class FaceForm(forms.ModelForm):
    class Meta:
        model = Face
        fields = ['face_img_test']
        labels = [
           {"face_img_test","登録写真"}
           ]