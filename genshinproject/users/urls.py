from django.urls import path
from users.forms import SetPasswordForm  
from users.views import Registration, MyLoginView
from django.urls import include
from django.contrib.auth import views 
urlpatterns = [
    path('', include('django.contrib.auth.urls'), name=''),
    path('registration/', Registration.as_view(), name='registration'),
    path('login', MyLoginView.as_view(),name='login'),
]