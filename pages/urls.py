from django.urls import path
from .views import Homepageview
from .views import AboutPageView

urlpatterns = [

    path("home/",Homepageview.as_view(),name="home"), 
    
    path("",AboutPageView.as_view(),name="about"),
    
] 