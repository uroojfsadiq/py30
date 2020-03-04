from django.shortcuts import render, redirect
from .models import Achievement, Testimonial, FormSubmission
import pandas as pd
import numpy as numpy
import tkinter as tk
from tkinter import filedialog
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.urls import reverse

def index(request):
    if request.method == "POST":
        form = FormSubmission()
        form.name = request.POST.get('name')
        form.phone = request.POST.get('phone')
        form.email = request.POST.get('email')
        form.message = request.POST.get('message')
        form.save()
    all_achievements = Achievement.objects.all()
    testim = Testimonial.objects.all() 
    return render(request, 'index.html', {'all_achievements' : all_achievements, 'testim' : testim})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def books(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        user_data = pd.read_csv(myfile.name)
        column_data = user_data.columns
        
        context = {
            'uploaded_file_url': uploaded_file_url,
            'user_data'        : user_data,
            'column_data'      : column_data
        }
        return render(request, 'books.html', context)
    return render(request, 'books.html')

def books_two(request):
    if request.method == 'POST':
        user_data   = pd.read_csv('books.csv')
        column_data = user_data.columns
        # csv_col_names = request.POST.getlist('csv_col_names')
        main_data = user_data[['age']]
        
        context = {
            # 'uploaded_file_url': uploaded_file_url,
            'user_data'        : user_data,
            'column_data'      : column_data,
            'main-data' : main_data
        }
        return render(request, 'books.html', context)

    return render(request, 'books.html')

