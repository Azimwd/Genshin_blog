from django.urls import path
from main.views import home, characters
from django.views.generic import TemplateView
urlpatterns = [
    path('', home, name='home'),
    path('home2', TemplateView.as_view(template_name='home2.html'), name='home2'),
    path('characters', characters, name='characters'),
    path('zhongli', TemplateView.as_view(template_name='characters_page/zhongli.html'), name='zhongli'),
]