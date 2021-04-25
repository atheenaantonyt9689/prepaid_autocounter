from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views import View
from .models import Place
from django.shortcuts import render
from .pre_paid import Place



class PlaceListView(ListView):
    model = Place
    template_name = 'core_section/home.html'

class PlaceView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"core_section/home.html",{})
        
    def post(self,request,*args,**kwargs):

        
        places_id=request.POST.get("Place.id")
        kms=Place.objects.get(id=places_id)
        #object creation 
        obj=Place(kms.places,kms.distance)

        context={'place_name':obj.place_name(),
        'amount':obj.amount(),
        'total_distance':obj.distance()

        }  

        reciept=Place.objects.create(place_name=place_name,amount=amount,total_distance=total_distance)
        pre_paid.save()     
        return render(request,"core_section/home.html",context)


        
        template_name = "core_section/home.html"

