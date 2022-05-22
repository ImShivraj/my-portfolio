from django.shortcuts import render, HttpResponse
from django.conf import settings
import os
# Create your views here.

file_path = os.path.join(settings.FILES_DIR)
def index(request):
    return HttpResponse('this is homepage')
