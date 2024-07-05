# predictor/views.py
from django.shortcuts import render
from .forms import LaptopFeatureForm
from .models import LaptopFeature
import joblib
import os

model_path =('laptop_price_model.joblib')
model = joblib.load(model_path)

def predict_form(request):
    form = LaptopFeatureForm()
    return render(request, 'predict.html', {'form': form})

def predict(request):
    if request.method == 'POST':
        form = LaptopFeatureForm(request.POST)
        if form.is_valid():
            laptop_feature = form.save(commit=False)
            features = [
                laptop_feature.processor_speed,
                laptop_feature.ram_size,
                laptop_feature.storage_capacity,
                laptop_feature.screen_size,
                laptop_feature.weight
            ]
            price = model.predict([features])[0]
            laptop_feature.predicted_price = price
            laptop_feature.save()
            return render(request, 'result.html', {'predicted_price': price})
    else:
        form = LaptopFeatureForm()
    return render(request, 'predict.html', {'form': form})
