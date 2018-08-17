# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Contact

from django.contrib import admin

class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')
# Register your models here.
admin.site.register(Contact, ContactAdmin)
