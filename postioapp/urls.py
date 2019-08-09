from django.urls import path
from .views import *

urlpatterns = [
     path('signup/', signup, name='signup'),
     path('login/', login, name='login'),
     path('logout/', logout, name='logout'),
     path('search/', main, name='search'),
     path('searchbar/', search, name='searchbar'),
     path('about/', about, name='about'),
     path('contact/', Contact, name='contact'),
]