from django.shortcuts import render
from .models import News, Slider

# Create your views here.

def home(request):
    news = News.objects.all()
    sliders = Slider.objects.all()
    categories = ['beauty', 'fashion and Style']
    context = {
        'news': news,
        'sliders': sliders,
        'categories': categories,

    }
    return render(request, 'index.html', context)


def beauty(request):
    news = News.objects.filter(category='beauty')


    return render(request, 'beauty.html', {'news': news})

def fashionAndStyle(request):
    news = News.objects.filter(category='fashion and Style')

    return render(request, 'fashion.html', {'news': news})



def detail(request, id):
    news = News.objects.get(pk=id)

    return render(request, 'blog-single.html', { 'news': news, 'test': "testing" })


def contactus(request):
    
    return render(request, 'contact.html')