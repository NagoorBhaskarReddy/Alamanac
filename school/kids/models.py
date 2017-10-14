# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Address(models.Model):
    house_number=models.CharField(max_length=20, null=True, blank=True)
    street=models.CharField(max_length=20, null=True, blank=True)
    area=models.CharField(max_length=20, null=True, blank=True)
    city=models.CharField(max_length=20, null=True, blank=True)
    state=models.CharField(max_length=20, null=True, blank=True)
    country=models.CharField(max_length=20, null=True, blank=True)
    pincode=models.CharField(max_length=10, null=True, blank=True)



class Student(models.Model):
	"""
	This is for student model
	"""
	name=models.CharField(max_length=10,null=True,blank=True)
	standard=models.CharField(max_length=10,null=True,blank=True)
	section=models.CharField(max_length=10,null=True,blank=True)
	status=models.BooleanField(default=True)
	age=models.IntegerField(null=True,blank=True)
	rollnumber=models.IntegerField(null=True,blank=True)
	dateofbirth=models.CharField(max_length=10, null=True,blank=True)
	address = models.ForeignKey('Address', null=True, blank=True)
	
class Parents(models.Model):
	p_name=models.CharField(max_length=20)
	p_age=models.IntegerField(null=True,blank=True)
	p_mobile=models.CharField(max_length=12,null=True,blank=True)
        p_email=models.CharField(max_length=12,null=True,blank=True)
	student=models.ForeignKey(Student,null=True,blank=True)

class Teacher(models.Model):
	t_name=models.CharField(max_length=20,null=True,blank=True)
	t_age=models.IntegerField(null=True,blank=True)
	email=models.EmailField(max_length=12,null=True,blank=True)
	address = models.ForeignKey(Address, null=True, blank=True)

class Uniform(models.Model):
	shirt_color=models.CharField(max_length=10,null=True,blank=True)
	phant_color=models.CharField(max_length=10,null=True,blank=True)
	shirt_size=models.IntegerField(null=True,blank=True)
	phant_size=models.IntegerField(null=True,blank=True)



class Attendances(models.Model):
    student_attendance = (
        ('Present', 'P'),
        ('Absent', 'A'),
    )
    date=models.DateField(max_length=20)
    attendance=models.CharField(choices=student_attendance, max_length=10, default='Present')
    student=models.ForeignKey(Student, null=True,blank=True)


class Signup(models.Model):
	f_name=models.CharField(max_length=20)
	l_name=models.CharField(max_length=20)
	email=models.CharField(max_length=12,null=True,blank=True)
	password=models.CharField(max_length=20,null=True,blank=True)
	r_password=models.CharField(max_length=20,null=True,blank=True)
	
