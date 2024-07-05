from django.urls import path
from . import views



urlpatterns=[
    path('',views.login,name="login"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('webpage',views.mainpage,name="webpage"),
    path('index',views.index,name="index"),
    path('map',views.map,name="map"),
    path('getDetails',views.getDetails,name="getDetails"),
    path('copymap',views.copymap,name="copymap"),
    path('overview',views.overview,name="overview"),
    path('calender',views.calender,name="calender"),
    path('hour',views.hour,name="hour"),
    path('rawdata',views.rawdata,name="rawdata"),
    path('compare',views.compare,name="compare"),
    path('about',views.about,name="about"),
    path('guide',views.guide,name="guide"),
    
]