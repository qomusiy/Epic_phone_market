from django.urls import path
from .views import home, phone_list, phone_detail, phone_add_form, contact_form, phone_edit, phone_delete

urlpatterns = [
    path('', home, name='home'),
    path('phone_list/', phone_list, name='phone_list'),
    path('phone/<int:pk>/', phone_detail, name='phone_detail'),
    path('phone_add/', phone_add_form, name='phone_add'),
    path('phone_edit/<int:pk>/', phone_edit, name='phone_edit'), 
    path('phone_delete/<int:pk>/', phone_delete, name='phone_delete'),
    path('contact/', contact_form, name='contact'),
]