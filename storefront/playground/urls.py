from django.urls import path
from . import views

#URLConf module - every app can have its own url configuration; end routes with forward slash
urlpatterns = [
    path('hello/', views.sayHello),
    path('hello2/', views.sayHello2)
]