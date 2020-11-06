from django.urls import path
from . import views

# app_name = 'upload_and_clean_excel'
   
urlpatterns = [
    # post views
    path('', views.upload, name='upload'),
]
