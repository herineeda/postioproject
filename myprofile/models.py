
# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User

class Career(models.Model):
    # 유저정보, 시작날짜, 종료날짜, 근무처, 직위, 내용
    c_author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_career', null=True, blank=True)
    start = models.DateField()
    end = models.DateField()
    office = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    text = models.TextField()
    
    def __str__(self):
        return self.text

class License(models.Model):
    # 유저정보, 자격취득날짜, 자격이름, 허가기관
    l_author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_license', null=True, blank=True)
    date = models.DateField()
    license_name = models.CharField(max_length=200)
    license_organ = models.CharField(max_length=400)
    
class Portfolio(models.Model):
    # 유저정보, 포트폴리오 사진, 사진 설명
    p_author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_portfolio', null=True, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    title_photo = models.CharField(max_length=200)
    text_photo = models.TextField()
    
    def __str__(self):
        return self.title_photo
        
    def summary(self):
        return self.text_photo[:50]

class Profile(models.Model):
    # 유저정보, 자기소개, 사진
    profile_photo = models.ImageField(upload_to='photos/profile/%Y/%m/%d')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_profile', null=True, blank=True)
    introduction = models.TextField()