from django import forms


class PriceForm(forms.Form):
    choices_waterfront = ((0,'NO'),(1,'YES'))
    choices_view = ((0,0),(1,1),(2,2),(3,3),(4,4))
    choices_condition = ((1,1),(2,2),(3,3),(4,4),(5,5))
    choices_grade = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13))
    
    yr_built = forms.IntegerField(label='Year built', min_value=1900,max_value=2023, required=True, initial=1900)
    yr_renovated = forms.IntegerField(label='Renovated in', min_value=0,max_value=2023, required=True, initial=0)
    zipcode = forms.IntegerField(label='Zipcode',min_value=98001,max_value=98199, required=True, initial=98001)
    lat = forms.FloatField(label='Latitude',min_value=47,max_value=48, required=True, initial=47.5)
    long = forms.FloatField(label='Longitude',required=True, initial=-122.5)
    sqft_living = forms.IntegerField(label='Building size',min_value=0, max_value=1740, required=True,initial=0)
    sqft_lot = forms.IntegerField(label='Lot size',min_value=0, max_value=1200, required=True,initial=0)
    sqft_basement = forms.IntegerField(label='Basement size',min_value=0, max_value=1660, required=True, initial=0)
    floors = forms.FloatField(label='Floors',min_value=1, max_value=3.5, required=True, initial=1)
    bedrooms = forms.IntegerField(label='Bedrooms', min_value=0, max_value=15, required=True, initial=0)
    bathrooms = forms.FloatField(label='Bathrooms',min_value=0.5, max_value=8.5, required=True, initial=0.5)
    waterfront = forms.TypedChoiceField(label='Waterfront',coerce=int, choices=choices_waterfront, required=True)
    view = forms.TypedChoiceField(label='View score', coerce=int, choices=choices_view, required=True, initial=1)
    condition = forms.TypedChoiceField(label='Condition score',coerce=int, choices=choices_condition, required=True, initial=2)
    grade = forms.TypedChoiceField(label='Grade score',coerce=int, choices=choices_grade, required=True, initial=7)


