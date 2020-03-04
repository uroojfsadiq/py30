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
empty = 'ds'


def books(request):
    global empty
    if request.method == 'POST' and request.FILES['myfile']:
        global empty
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        user_data = pd.read_csv(myfile.name)
        column_data = user_data.columns
        values_data = user_data.values
        empty = uploaded_file_url
        # print(empty)
        
        context = {
            'uploaded_file_url': uploaded_file_url,
            'user_data'        : user_data,
            'column_data'      : column_data,
            'values_data' : values_data
        }
        return render(request, 'books.html', context)
    return render(request, 'books.html')

def books_two(request):
    global empty
    print(empty)

    if request.method == 'POST':
        csv_col_names = request.POST.getlist('csv_col_names')
        print(empty)
        print(f'./{empty}')
        user_data   = pd.read_csv(f'./{empty}', usecols=csv_col_names)

        # column_data = user_data.columns
        # csv_col_names = request.POST.getlist('csv_col_names')
        # main_data = user_data[['age']]
        
        context = {
            # 'uploaded_file_url': uploaded_file_url,
            # 'user_data'        : user_data,
            # 'column_data'      : column_data
            'main_data' : user_data,
        }
        return render(request, 'books.html', context)

    return render(request, 'books.html')

