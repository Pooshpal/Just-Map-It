from django.urls import path
from .views import get_map, get_metadata,  get_directions,get_all_records,get_image

urlpatterns = [
    path('getMap/', get_map, name='get_map'),
    path('getMetadata/', get_metadata, name='get_metadata'),
    path('getDirections/', get_directions, name='get_directions'),
    path('getVisualization/', get_image, name='get_image'),
    
    path('all/', get_all_records, name='get_all_records'),
]
