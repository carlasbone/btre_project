from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),                     # /listings     will get the index.html from the listings folder
    path('<int:listing_id>', views.listing, name='listing'),     # /listings/listing_id
    path('search', views.search, name='search'),
]
