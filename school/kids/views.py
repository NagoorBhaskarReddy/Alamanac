from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from kids.models import *
from django.contrib.auth import authenticate
from django.utils.timezone import datetime #important if using timezones
from .forms import StudentFrom
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from kids.serializers import UserSerializer, GroupSerializer, StudentSerializer
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class Signups(View):
    template_name="school.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
	f_name=request.POST.get('f_name')
	l_name=request.POST.get('l_name')
	email=request.POST.get('email')
	password=request.POST.get('password')
	r_password=request.POST.get('r_password')
	s_obj=Signup()
	s_obj.f_name=f_name
	s_obj.l_name=l_name
	s_obj.email=email
	s_obj.password=password
	s_obj.r_password=r_password
	s_obj.save()
	return render(request, self.template_name, locals())

class Login(View):
    template_name="index.html"
    def post(self, request, *args, **kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        #user=authenticate(username, password)
        return render(request, self.template_name, locals())

class Students(View):
    template_name="student.html"
    def get(self, request, *args, **kwargs):
        students=Student.objects.all()
        serializer_class = StudentSerializer
	
        return render(request, self.template_name, locals())
    def post(self, request, *args, **kwargs):
        name=request.POST.get('name')
	standard=request.POST.get('standard')
	section=request.POST.get('section')
	houseName=request.POST.get('housename')
	age=request.POST.get('age')
	rollnumber=request.POST.get('rollnumber')
	dateofbirth=request.POST.get('dob')
        
	house_number=request.POST.get('house_number')
	street=request.POST.get('street')
	area=request.POST.get('area')
	city=request.POST.get('city')
	state=request.POST.get('state')
	country=request.POST.get('country')
	pincode=request.POST.get('pincode')

	stud_obj=Student()
	a_obj=Address()
        stud_obj.name=name
        stud_obj.standard=standard
        stud_obj.section=section
        stud_obj.houseName=houseName
        stud_obj.age=age
        stud_obj.status=True
        stud_obj.rollnumber=rollnumber
        stud_obj.dateofbirth=dateofbirth
	a_obj.house_number=house_number
	a_obj.street=street
	a_obj.area=area
	a_obj.city=city
	a_obj.state=state
	a_obj.country=country
	a_obj.pincode=pincode
	a_obj.save()
        stud_obj.address=a_obj
        stud_obj.save()	
        return render(request, self.template_name, locals())


class Parent(View):
    template_name="parent.html"
    def get(self, request, *args, **kwargs):	
        parents=Parents.objects.all()
        students=Student.objects.all()
	return render(request, self.template_name, locals())
    def post(self,request,*args,**kwargs):
	stud_id=request.POST.get('student')
	p_name=request.POST.get('p_name')
	p_age=request.POST.get('p_age')
	p_mobile=request.POST.get('p_mobile')
	p_email=request.POST.get('p_email')
	p_obj=Parents()
        stud_obj=Student.objects.get(id=stud_id)
	p_obj.p_name=p_name
	p_obj.p_age=p_age
	p_obj.p_mobile=p_mobile
	p_obj.p_email=p_email
        p_obj.student=stud_obj 
	p_obj.save()
	return render(request,self.template_name,locals())

class Uniforms(View):
    template_name="uniform.html"
    def get(self,request,*args, **kwargs):
	uniform=Uniform.objects.all()
	return render(request, self.template_name, locals())
    def post(self,request, *args, **kwargs):
	shirt_color=request.POST.get('shirt_color')
	phant_color=request.POST.get('phant_color')
	shirt_size=request.POST.get('shirt_size')
	phant_size=request.POST.get('phant_size')
	uni_obj=Uniform()
	uni_obj.shirt_color=shirt_color
	uni_obj.phant_color=phant_color
	uni_obj.shirt_size=shirt_size
	uni_obj.phant_size=phant_size
	uni_obj.save()
	return render(request,self.template_name,locals())

class Teachers(View):
    template_name="teacher.html"
    def get(self, request, *args, **kwargs):
	teachers=Teacher.objects.all()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
	t_name=request.POST.get('t_name')
	t_age=request.POST.get('t_age')
	email=request.POST.get('email')

	house_number=request.POST.get('house_number')
	street=request.POST.get('street')
	area=request.POST.get('area')
	city=request.POST.get('city')
	state=request.POST.get('state')
	country=request.POST.get('country')
	pincode=request.POST.get('pincode')

	t_obj=Teacher()
	a_obj=Address()
	t_obj.t_name=t_name
	t_obj.t_age=t_age
	t_obj.email=email

	a_obj.house_number=house_number
	a_obj.street=street
	a_obj.area=area
	a_obj.city=city
	a_obj.state=state
	a_obj.country=country
	a_obj.pincode=pincode
	a_obj.save()
        t_obj.address=a_obj	

	t_obj.save()
	return render(request,self.template_name,locals())


class Attendance(View):
    template_name="attendance.html"
    def get(self,request, *args, **kwargs):
        today = datetime.today()
        print(today.date())
        students=Student.objects.all()
	attendance=Attendances.objects.filter(date=today.date())
	return render(request, self.template_name, locals())

    def post(self, request, *args , **kwargs):
	stud_id=request.POST.getlist('stud_id[]')
	date=request.POST.get('date')
	attendance=request.POST.getlist('attendance[]')
        print(attendance)
        for ls in range(len(stud_id)):
            try:
	       at_obj=Attendances()
	       stud_obj=Student.objects.get(id=stud_id[ls])
	       at_obj.date=date
	       at_obj.attendance=attendance[ls]
	       at_obj.student=stud_obj
	       at_obj.save()
            except:
               continue
        students=Student.objects.all()
	attendance=Attendances.objects.filter(date='2017-10-06')
	return render(request, self.template_name, locals())


class Contact(View):
    template_name="contact.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())


class Gallery(View):
    template_name="gallery.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())


class Studentss(View):
    template_name="students.html"
    def get(self, request, *args, **kwargs):
	form = StudentFrom()
        return render(request, self.template_name, locals())


