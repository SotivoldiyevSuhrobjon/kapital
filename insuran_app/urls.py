from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page, name='home'),
    path('osago/', views.osago_page, name='osago'),
    path('sport/', views.sport_page, name='sport'),
    path('personal/', views.personal_page, name='personal'),
    path('accident/', views.accident_page, name='accident'),
    path('travel/', views.travel_page, name='travel'),
    path('cities/<int:region_id>/', views.get_cities, name='get_cities'),
    path('related-sports/<int:sport_id>/', views.get_related_sports, name='get_related_sports'),
    
]
