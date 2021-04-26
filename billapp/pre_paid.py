class PrePaid:
    min_distance=1.5
    min_charge=20

    def __init__(self,places,distance):
        self.places=places
        self.distance=distance
    def place_name(self):
        return self.places
    
    """def amount(self):
        if distance>Place.min_distance:
            total_distance=self.distance/Place.min_distance
            total_price=total_distance*Place.min_charge            
            return total_price

        else:
             return Place.min_charge """  
    def distance(self):
        total_distance=self.distance/PrePaid.min_distance
        return total_distance
    def amount(self):
        return self.distance()*PrePaid.min_charge
   




    

             

#places="kdr"
#distance=3
#obj=User(places,distance)
#obj.total_price()



