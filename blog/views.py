# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import os

# Create your views here.
def post_list(request):
	print (os.getcwd())
	return render(request, 'blog/post_list.html')
