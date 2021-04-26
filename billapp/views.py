from django.http import Http404
from django.views.generic import TemplateView
#from django.views.generic import ListView
from django.views import View
from .models import Place
from django.shortcuts import render,get_object_or_404
from .pre_paid import PrePaid
class PlaceView(View):
    model=Place
    def get(self,request,*args,**kwargs):
        place = Place.objects.get("place.id")
        print (place.id)

        #obj=get_object_or_404(Place,id=id)

        #try:
            #obj=Place.objects.get
            #obj=Place.objects.get("")
            #place_list=Place.objects.all()
        #except Place.DoesNotExist:

            #raise Http404
        """try:
            #id = self.kwargs.get("id")
            places_id=request.GET.get(place.id)
            obj=Place.objects.get(id=id)
        except Place.DoesNotExist:
            raise Http404
        context={
            "object":obj
        }
"""
        
        return render(request,"core_section/home.html",context)
        
    def post(self,request,*args,**kwargs):

        places_id=request.POST.get("place.id")
        kms=Place.objects.get(id=places_id)
        #object creation 
        obj=PrePaid(kms.places,kms.distance)

        context={
        #'place_list'  :place_list ,    
        'place_name':obj.place_name(),
        'amount':obj.amount(),
        'total_distance':obj.distance()
        }  
        reciept=Place.objects.create(place_name=place_name,amount=amount,total_distance=total_distance)
        reciept.save()     
        return render(request,"core_section/home.html",context)


        
        template_name = "core_section/home.html"

