"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from kids.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', Signups.as_view()),
    url(r'^login/', Login.as_view()),
    url(r'^student/',Students.as_view()),
    url(r'^student_list/',Students.as_view()),
    url(r'^parents/',Parent.as_view()),
    url(r'^uniform/',Uniforms.as_view()),
    url(r'^teacher/',Teachers.as_view()),
    url(r'^attendance/',Attendance.as_view()),
    url(r'^contact/',Contact.as_view()),
    url(r'^gallery/',Gallery.as_view()),
    url(r'^students/',Studentss.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
