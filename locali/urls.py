from django.urls import path
from . import views

urlpatterns = [
    path('api/locali/', views.LocaleList.as_view() ),
    path('api/comuni/', views.ComuniList.as_view() ),
]
