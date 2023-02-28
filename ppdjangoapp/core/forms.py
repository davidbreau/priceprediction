from django import forms


class PriceForm(forms.Form):
    choices_waterfront = ((0,'NON'),(1,'OUI'))
    choices_view = ((0,0),(1,1),(2,2),(3,3),(4,4))
    choices_condition = ((1,1),(2,2),(3,3),(4,4),(5,5))
    choices_grade = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13))
    
    bedrooms = forms.IntegerField(min_value=0, max_value=15, required=True)
    bathrooms = forms.FloatField(min_value=0.5, max_value=8.5, required=True)
    sqft_living = forms.IntegerField(min_value=0, max_value=1740, required=True)
    sqft_lot = forms.IntegerField(min_value=0, max_value=1200, required=True)
    floors = forms.FloatField(min_value=1, max_value=3.5, required=True)
    waterfront = forms.TypedChoiceField(coerce=int, choices=choices_waterfront, required=True)
    view = forms.TypedChoiceField(coerce=int, choices=choices_view, required=True)
    condition = forms.TypedChoiceField(coerce=int, choices=choices_condition, required=True)
    grade = forms.TypedChoiceField(coerce=int, choices=choices_grade, required=True)
    sqft_basement = forms.IntegerField(min_value=0, max_value=1660, required=True)
    yr_built = forms.IntegerField(min_value=1900,max_value=2023, required=True)
    yr_renovated = forms.IntegerField(min_value=1900,max_value=2023, required=True)
    zipcode = forms.IntegerField(min_value=98001,max_value=98199, required=True)
    lat = forms.FloatField(min_value=47,max_value=48, required=True)
    long = forms.FloatField(required=True)