from django.urls import path
from tours import views

urlpatterns = [
    path('', views.main_view),
    path('tour/<int:id>/', views.tour_view),
    path('departure/<str:departure>/', views.departure_view),
]
