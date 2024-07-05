from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from AQMapp.models import EVChargingLocation
from geopy.distance import geodesic
# Create your views here.
def index(request):
    return render(request,'index.html')


def dashboard(request):
    return render(request,'base.html')

def overview(request):
    return render(request,'overview.html')

def calender(request):
    return render(request,'calender.html')

def rawdata(request):
    return render(request,'rawdata.html')

def hour(request):
    return render(request,'hour.html')


def compare(request):
    return render(request,'compare.html')

def guide(request):
    return render(request,'guide.html')

def about(request):
    return render(request,'about.html')

def mainpage(request):
    return render(request,'webpage.html')

def login(request):
    return render(request,'login.html')

def map(request):
    stations=list(EVChargingLocation.objects.values('latitude','longitude')[:100])
    context = {'stations':stations}
    return render(request,'map_own.html',context)

def getDetails(request):
    lat=request.GET.get('lat')
    lon=request.GET.get('lon')
    print(lat,lon)
    data=json.loads(request.body)
    return render(request, 'display_data.html', {'data': data})

def copymap(request):
    return render(request,'map.html')