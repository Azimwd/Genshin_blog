from django.urls import path
from main.views import home
from django.views.generic import TemplateView
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]