from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib import admin
from .models import Student

def index(request):
    return HttpResponse("Hello, world. You're at the reldb_app index.")

#admin.site.register(Student)