from django.urls import path
from .views import PlaceView
urlpatterns = [
path('',PlaceView.as_view(),name='place'),
    
#path('', PlaceListView.as_view(),name='place')
]