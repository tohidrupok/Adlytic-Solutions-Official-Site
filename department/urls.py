from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('details/<slug:category_slug>/', views.details, name='details'),
   path('buy/<int:id>/', views.buy, name='buy'),
   path('about/', views.about, name='about'),
   path('portfolio/', views.portfolio, name='portfolio'),
   path('team/', views.team_member, name='team'),
    
] 
