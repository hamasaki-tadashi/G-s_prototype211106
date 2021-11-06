from django.db import models

# 投稿できるフォーマット、型、クラスの作成


class Post(models.Model):
    title = models.CharField('タイトル', max_length=50)
    content = models.TextField('内容', max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Postの内容をタイトルを使って参照できるようにする
    def __str__(self):
        return self.title
