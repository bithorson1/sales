from django.urls import path
from . import views

urlpatterns = [
    path('api/refresh_data/', views.trigger_data_refresh, name='refresh_data'),
    path('api/revenue/', views.get_revenue, name='get_revenue'),
    path('api/top_products/', views.get_top_products, name='top_products'),
]
