# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here:

class Contact(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField() 
    phone_number = models.CharField(max_length = 10, blank = True, null = True) 
    description = models.CharField(max_length = 3000, blank = True, null = True)

    def __unicode__(self):
        return u'%s' % self.name

class Blog(models.Model):
    blog_name  = models.CharField(max_length=25, blank=True, null=True)
    blog_image = models.ImageField(upload_to = "blogs/Blog/Images")
    blog_description = models.CharField(max_length=30000, blank=True, null=True)


