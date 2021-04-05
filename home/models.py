from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY = (
    ('beauty', 'beauty'),
    ('fashion and Style', 'fashion and style')
)

class News(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    isTrending = models.BooleanField(default=False)
    isEditorPick = models.BooleanField(default=False)
    category = models.CharField(max_length=124, choices=CATEGORY)
    image = models.ImageField(upload_to="news_thumbnail")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[0:14]+"..."

class Slider(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    category = models.CharField(max_length=125, choices=CATEGORY)
    image = models.ImageField(upload_to="sliders")


    def __str__(self):
        return self.title[0:14]+"..."