from django.shortcuts import render
# from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar


def index(request):
  
    return render(request, 'challenge/base.html')
    