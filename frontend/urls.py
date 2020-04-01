from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path('about.html', views.about ),
    path('create/', views.LocaleFormView.as_view(), name='create-locale'),

]
