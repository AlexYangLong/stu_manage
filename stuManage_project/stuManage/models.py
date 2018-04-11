# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Admin(models.Model):
    id = models.BigAutoField(primary_key=True)
    ad_number = models.CharField(max_length=16, blank=True, null=True)
    ad_name = models.CharField(max_length=20, blank=True, null=True)
    ad_password = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'

    @classmethod
    def createAdmin(cls, number, name, password):
        admin = cls(ad_number=number, ad_name=name, ad_password=password)
        return admin


class DormType(models.Model):
    id = models.BigAutoField(primary_key=True)
    d_type = models.CharField(max_length=8, blank=True, null=True)
    d_price = models.IntegerField(blank=True, null=True)
    d_addtime = models.DateTimeField(blank=True, null=True)
    d_edittime = models.DateTimeField(blank=True, null=True)
    d_editadmin = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dorm_type'

    @classmethod
    def createDormType(cls, type, price, addtime, edittime, editadmin):
        dormType = cls(d_type=type, d_price=price, d_addtime=addtime, d_edittime=edittime, d_editadmin=editadmin)
        return dormType

class Dormitory(models.Model):
    id = models.BigAutoField(primary_key=True)
    d_number = models.CharField(max_length=8, blank=True, null=True)
    d_position = models.CharField(max_length=36, blank=True, null=True)
    d_dormtype = models.BigIntegerField(blank=True, null=True)
    d_isempty = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'dormitory'

    @classmethod
    def createDormitory(cls, number, position, dormtype, isempty):
        dorm = cls(d_number=number, d_position=position, d_dormtype=dormtype, d_isempty=isempty)
        return dorm

class FeeType(models.Model):
    id = models.BigAutoField(primary_key=True)
    f_type = models.CharField(max_length=8, blank=True, null=True)
    f_price = models.IntegerField(blank=True, null=True)
    f_addtime = models.DateTimeField(blank=True, null=True)
    f_edittime = models.DateTimeField(blank=True, null=True)
    f_editadmin = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fee_type'

    @classmethod
    def createFeeType(cls, type, price, addtime, edittime, editadmin):
        feeType = cls(f_type=type, f_price=price, f_addtime=addtime, f_edittime=edittime, f_editadmin=editadmin)
        return feeType


class StuDorm(models.Model):
    id = models.BigAutoField(primary_key=True)
    stu_id = models.BigIntegerField(blank=True, null=True)
    dorm_id = models.BigIntegerField(blank=True, null=True)
    dorm_isuse = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'stu_dorm'

    @classmethod
    def createStuDorm(cls, stu_id, dorm_id, dorm_isuse):
        stuDorm = cls(stu_id=stu_id, dorm_id=dorm_id, dorm_isuse=dorm_isuse)
        return stuDorm


class StuFee(models.Model):
    id = models.BigAutoField(primary_key=True)
    study_fee = models.BooleanField(default=False)
    dinner_fee = models.BooleanField(default=False)
    insurance_fee = models.BooleanField(default=False)
    other_fee = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'stu_fee'

    @classmethod
    def createStuFee(cls, study_fee, dinner_fee, insurance_fee, other_fee):
        stuFee = cls(study_fee=study_fee, dinner_fee=dinner_fee,insurance_fee=insurance_fee,other_fee=other_fee)
        return stuFee


class Students(models.Model):
    id = models.BigAutoField(primary_key=True)
    s_number = models.CharField(max_length=16, blank=True, null=True)
    s_name = models.CharField(max_length=20, blank=True, null=True)
    s_gender = models.IntegerField(blank=True, null=True)
    s_age = models.IntegerField(blank=True, null=True)
    s_intro = models.CharField(max_length=200, blank=True, null=True)
    s_idnumber = models.CharField(db_column='s_Idnumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s_address = models.CharField(max_length=80, blank=True, null=True)
    s_phone = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'

    @classmethod
    def createStudent(cls, number, name, gender, age, intro, idnumber, address, phone):
        stu = cls(s_number=number, s_name=name, s_gender=gender,s_age=age, s_intro=intro, s_idnumber=idnumber, s_address=address, s_phone=phone)
        return stu