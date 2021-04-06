from django.urls import path
from .views import home, beauty,fashionAndStyle, detail, contactus


urlpatterns = [
    path('', home, name="home" ),
    path('beauty/', beauty, name="beauty"),
    path('fashion-and-style/', fashionAndStyle, name="fashion-and-style"),
    path('detail-post/<int:id>/', detail, name="detail-post"),
    path('contactus/', contactus, name="contactus")
]