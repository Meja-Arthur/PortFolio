from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.get_users, name='get_users'),
    path('user/<uuid:user_id>/', views.get_user_by_id, name='get_user_by_id'),
    # Other URL patterns for your views can be added here
]