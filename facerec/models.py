import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

days = 365

class Face(models.Model):
    user_name = models.CharField(max_length=100)
    # 画像をアップロード時にはpillowライブラリが使われるので、pipでインストールする必要あり
    # 前提としてブランクの時にはデフォルトでどこに保存するかの設定をsettings.pyに書き込む必要あり
    face_img_train = models.ImageField(upload_to='') # upload_toはどこのディレクトリに画像をアップロードするかの設定
    face_img_test = models.ImageField(upload_to='') # upload_toはどこのディレクトリに画像をアップロードするかの設定
    pub_date = models.DateTimeField("date published")
    def __str__(self):
          return self.user_name
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published within " + str(days) + " days?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days) <= self.pub_date <= now
    