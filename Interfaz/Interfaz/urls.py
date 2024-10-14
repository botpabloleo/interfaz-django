from django.urls import path
from Interfazz.views import index, citas, contacto, cortes, login, register

urlpatterns = [
    path('', index, name='index'),
    path('citas/', citas, name='citas'),
    path('contacto/', contacto, name='contacto'),
    path('cortes/', cortes, name='cortes'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]