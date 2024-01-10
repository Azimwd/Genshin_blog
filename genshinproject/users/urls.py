from django.urls import path
from users.forms import MyLoginView    
from users.views import Registration
from django.urls import include
urlpatterns = [
    path('', include('django.contrib.auth.urls'), name=''),
    path('registration/', Registration.as_view(), name='registration'),
    # path('login', MyLoginView.as_view(),name='login'),
]
