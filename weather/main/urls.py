# from django.urls import path
# from .views import hello_view

# urlpatterns = [
#     path('', hello_view, name='hello'),
# ]

from django.urls import path 
from . import views 

urlpatterns = [ 
		path('', views.index), 
] 
