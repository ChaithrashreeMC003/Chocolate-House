from django.urls import path
from .import views

urlpatterns=[
    path('',views.index),
    path('seasonalFlavor/',views.flavors),
    path('ingredient/',views.inventory),
    path('customer/',views.suggestions),

    
]