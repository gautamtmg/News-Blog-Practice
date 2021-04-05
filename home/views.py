from django.shortcuts import render
from .models import News, Slider

# Create your views here.

def home(request):
    news = News.objects.all()
    sliders = Slider.objects.all()
    context = {
        'news': news,
        'sliders': sliders
    }
    return render(request, 'index.html', context)
