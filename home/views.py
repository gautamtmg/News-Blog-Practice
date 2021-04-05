from django.shortcuts import render
from .models import News, Slider

# Create your views here.

def home(request):
    news = News.objects.all()
    sliders = Slider.objects.all()
    categories = ['Beauty', 'Fashion and Style', 'Food']
    context = {
        'news': news,
        'sliders': sliders,
        'categories': categories,

    }
    return render(request, 'index.html', context)
