from django.db import models

class Home(models.Model):
    choices_waterfront = ((0,'NON'),(1,'OUI'))
    choices_view = ((0,0),(1,1),(2,2),(3,3),(4,4))
    choices_condition = ((1,1),(2,2),(3,3),(4,4),(5,5))
    choices_grade = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13))
    
    bedrooms = models.IntegerField(blank=False, null=False)
    bathrooms = models.FloatField(blank=False, null=False)
    sqft_living = models.IntegerField(blank=False, null=False)
    sqft_lot = models.IntegerField(blank=False, null=False)
    floors = models.FloatField(blank=False, null=False)
    waterfront = models.CharField(max_length=1, choices=choices_waterfront, blank=False, null=False)
    view = models.CharField(max_length=1, choices=choices_view, blank=False, null=False)
    condition = models.CharField(max_length=1,choices=choices_condition, blank=False, null=False)
    grade = models.CharField(max_length=2,choices=choices_grade, blank=False, null=False)
    sqft_basement = models.IntegerField(blank=False, null=False)
    yr_built = models.IntegerField(blank=False, null=False)
    yr_renovated = models.IntegerField(blank=False, null=False)
    zipcode = models.IntegerField(blank=False, null=False)
    lat = models.FloatField(blank=False, null=False)
    long = models.FloatField(blank=False, null=False)