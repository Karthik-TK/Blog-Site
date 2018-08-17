# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
# Create your views here.
@csrf_protect
def home_page(request):
    html = "home.html"
    return  render(request, html)

@csrf_protect
def blog_page(request):
    html = "blogs.html"
    return  render(request, html)
    
@csrf_protect    
def Contact_us_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')

    else:
        form =ContactForm()

    return render(request, "contact.html", {'form': form})