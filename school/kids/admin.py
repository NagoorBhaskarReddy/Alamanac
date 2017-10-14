# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from kids.models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Parents)
admin.site.register(Teacher)
admin.site.register(Uniform)
admin.site.register(Attendances)
admin.site.register(Address)
admin.site.register(Signup)

