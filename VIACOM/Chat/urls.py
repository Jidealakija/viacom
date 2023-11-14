from django.urls import path
from .views import contact, home, contact2, contact3


urlpatterns = [
    path('', home, name = 'home'),
    path('contact/', contact, name = 'contact'),
    path('contact2/', contact2, name = 'contact2'),
    path('contact3/', contact3, name = 'contact3')
]