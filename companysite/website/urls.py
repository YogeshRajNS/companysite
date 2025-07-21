from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('contact/', views.contact_view, name='contact'),
    path('submit/', views.submit_view, name='submit'),  # ✅ lowercase and ends with slash
]
