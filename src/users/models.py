from django.db import models

# Create your models here.

class RegionModel(models.Model):
    id = models.IntegerField(primary_key=True)
    학년구분 = models.CharField(max_length=30)
    학교명 = models.CharField(max_length=30)
    학교종류 = models.CharField(max_length=30)
    nt = models.FloatField()
    nnt = models.FloatField()
    nnnt = models.FloatField()
    행정구 = models.CharField(max_length=30)

class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    학년구분 = models.CharField(max_length=30)
    학교명 = models.CharField(max_length=30)
    학교종류 = models.CharField(max_length=30)
    nt = models.FloatField()
    nnt = models.FloatField()
    nnnt = models.FloatField()
    행정구 = models.CharField(max_length=30)

class Babyies(models.Model):
    id = models.IntegerField(primary_key=True)
    출생년도 = models.FloatField()
    입학년도 = models.FloatField()
    ARIMA = models.FloatField()
    SSM = models.FloatField()
    DLDA = models.FloatField()

class B(models.Model):
    id = models.IntegerField(primary_key=True)
    출생년도 = models.FloatField()
    입학년도 = models.FloatField()
    ARIMA = models.FloatField()
    SSM = models.FloatField()
    DLDA = models.FloatField()

class S(models.Model):
    id = models.IntegerField(primary_key=True)
    학년구분 = models.CharField(max_length=30)
    학교명 = models.CharField(max_length=30)
    학교종류 = models.CharField(max_length=30)
    nt = models.FloatField()
    nnt = models.FloatField()
    nnnt = models.FloatField()
    행정구 = models.CharField(max_length=30)

class R1(models.Model):
    id = models.IntegerField(primary_key=True)
    예측년도 = models.FloatField()
    월배 = models.FloatField()
    성서 = models.FloatField()
    수성 = models.FloatField()
    칠곡 = models.FloatField()
    동부 = models.FloatField()
    서부 = models.FloatField()
    북부 = models.FloatField()
    남부 = models.FloatField()
    동대구 = models.FloatField()
    달성 = models.FloatField()
    중부 = models.FloatField()
    모델 = models.CharField(max_length=30)

class R2(models.Model):
    id = models.IntegerField(primary_key=True)
    예측년도 = models.FloatField()
    월배 = models.FloatField()
    성서 = models.FloatField()
    수성 = models.FloatField()
    칠곡 = models.FloatField()
    동부 = models.FloatField()
    서부 = models.FloatField()
    북부 = models.FloatField()
    남부 = models.FloatField()
    동대구 = models.FloatField()
    달성 = models.FloatField()
    중부 = models.FloatField()
    모델 = models.CharField(max_length=30)

class R3(models.Model):
    id = models.IntegerField(primary_key=True)
    예측년도 = models.FloatField()
    월배 = models.FloatField()
    성서 = models.FloatField()
    수성 = models.FloatField()
    칠곡 = models.FloatField()
    동부 = models.FloatField()
    서부 = models.FloatField()
    북부 = models.FloatField()
    남부 = models.FloatField()
    동대구 = models.FloatField()
    달성 = models.FloatField()
    중부 = models.FloatField()
    모델 = models.CharField(max_length=30)

class R4(models.Model):
    id = models.IntegerField(primary_key=True)
    예측년도 = models.FloatField()
    월배 = models.FloatField()
    성서 = models.FloatField()
    수성 = models.FloatField()
    칠곡 = models.FloatField()
    동부 = models.FloatField()
    서부 = models.FloatField()
    북부 = models.FloatField()
    남부 = models.FloatField()
    동대구 = models.FloatField()
    달성 = models.FloatField()
    중부 = models.FloatField()
    모델 = models.CharField(max_length=30)

class R5(models.Model):
    id = models.IntegerField(primary_key=True)
    예측년도 = models.FloatField()
    월배 = models.FloatField()
    성서 = models.FloatField()
    수성 = models.FloatField()
    칠곡 = models.FloatField()
    동부 = models.FloatField()
    서부 = models.FloatField()
    북부 = models.FloatField()
    남부 = models.FloatField()
    동대구 = models.FloatField()
    달성 = models.FloatField()
    중부 = models.FloatField()
    모델 = models.CharField(max_length=30)

class R6(models.Model):
    id = models.IntegerField(primary_key=True)
    예측년도 = models.FloatField()
    월배 = models.FloatField()
    성서 = models.FloatField()
    수성 = models.FloatField()
    칠곡 = models.FloatField()
    동부 = models.FloatField()
    서부 = models.FloatField()
    북부 = models.FloatField()
    남부 = models.FloatField()
    동대구 = models.FloatField()
    달성 = models.FloatField()
    중부 = models.FloatField()
    모델 = models.CharField(max_length=30)