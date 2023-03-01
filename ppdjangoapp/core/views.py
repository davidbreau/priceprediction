from django.shortcuts import render
from django import forms
import datetime
import pandas as pd
import pickle
from .forms import PriceForm

with open('trained_pipe.pkl', 'rb') as f:
    model = pickle.load(f)

def index(request):
    form = PriceForm
    if request.method == 'POST':
        form = PriceForm(request.POST)
        if form.is_valid():
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            sqft_living = form.cleaned_data['sqft_living']
            sqft_lot = form.cleaned_data['sqft_lot']
            floors = form.cleaned_data['floors']
            waterfront = form.cleaned_data['waterfront']
            view = form.cleaned_data['view']
            condition = form.cleaned_data['condition']
            grade = form.cleaned_data['grade']
            sqft_basement = form.cleaned_data['sqft_basement']
            yr_built = form.cleaned_data['yr_built']
            yr_renovated = form.cleaned_data['yr_renovated']
            zipcode = form.cleaned_data['zipcode']
            lat = form.cleaned_data['lat']
            long = form.cleaned_data['long']
            
            sqft_above = sqft_living - sqft_basement
            yr_gap = int(datetime.date.today().strftime("%Y")) - max(yr_built, yr_renovated)
            
            X = pd.DataFrame({
            'bedrooms': [bedrooms],
            'bathrooms' : [bathrooms],
            'sqft_living' : [sqft_living],
            'sqft_lot' : [sqft_lot],
            'floors' : [floors],
            'waterfront' : [waterfront],
            'view' : [view],
            'condition' : [condition],
            'grade' : [grade],
            'sqft_above' : [sqft_above],
            'yr_built' : [yr_built],
            'yr_renovated' : [yr_renovated],
            'zipcode' : [zipcode],
            'lat' : [lat],
            'long' : [long],
            'yr_gap' : [yr_gap],
            })
            
            price_prediction = model.predict(X)[0]
            return render(request, 'core/result.html', {'price_prediction': price_prediction})
    else:
        form = PriceForm()
    return render(request, 'core/index.html', context={'form': form})

