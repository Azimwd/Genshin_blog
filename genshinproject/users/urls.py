from django.urls import path
from users.views import Registration
from django.urls import include
urlpatterns = [
    path('', include('django.contrib.auth.urls'), name=''),
    path('registration/', Registration.as_view(), name='registration')
]
