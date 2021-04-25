from django.urls import path
from .views import PlaceListView,PlaceView
urlpatterns = [
path('',PlaceView.as_view(),name='receipt'),
    
path('', PlaceListView.as_view(),name='places')
]