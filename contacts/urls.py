from django.urls import path
from contacts.views import contact

urlpatterns = [
    path('contact/', contact, name='contact'),
]
