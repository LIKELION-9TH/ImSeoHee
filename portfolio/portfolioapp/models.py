from django.db import models

# Create your models here.
from embed_video.fields import EmbedVideoField 

class Hobby(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title

class Place(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

# Music 모델로 Youtube Api 사용시 재생오류 발생 
#class Music(models.Model):
#    title = models.CharField(max_length=200)
#    singer = models.CharField(max_length=200,default = '')
#    music_key = models.CharField(max_length=12)

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title

# 유튜브 영상 재생
# 유튜브 Music 영상 Post
class Post(models.Model): 
    title = models.CharField(max_length=200) 
    singer = models.CharField(max_length=200) 
    video = EmbedVideoField()
#    lyrics = models.TextField(default = '')

class Visit(models.Model): 
    title = models.CharField(max_length=200) 
    write_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


