from django.urls import path
from main.views import home, charapters
from django.views.generic import TemplateView
urlpatterns = [
    path('', home, name='home'),
    path('home2', TemplateView.as_view(template_name='home2.html'), name='home2'),
    path('charapters', charapters, name='charapters'),
]