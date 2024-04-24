from django.urls import path
from . import views

app_name = 'summarizer'

urlpatterns = [
    path('', views.upload_text, name='upload_text'),
    path('result/<int:pk>/', views.text_detail, name='result'),
]
