from django.urls import path
from . import views
# Les urls sont composées de de l'id de l'image
urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.image, name='image'),
]