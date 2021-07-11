from django.urls import path
from django.urls.resolvers import URLPattern
from .views import HomePageView
from .views import AboutUsPageView

urlpatterns=[
  path ('' , HomePageView.as_view() , name ='home') , 
  path ('about', AboutUsPageView.as_view(), name='about')
]