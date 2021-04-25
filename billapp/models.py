from django.db import models


# Create your models here.
class Place(models.Model):
    places= models.CharField(max_length=100)
    distance=models.CharField(max_length=100)

    
    def __str__(self):
        return self.places
    #def get_absolute_url(self):
        #return reverse('reciept', args=[str(self.id)])


  


