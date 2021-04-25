from django.urls import path
from .views import PlaceListView,PlaceView
urlpatterns = [
path('placess',PlaceView.as_view(),name='receipt'),
    
path('', PlaceListView.as_view(),name='place')
]