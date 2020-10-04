from django.urls import path
from tours import views

urlpatterns = [
    path('', views.mainView),
    path('tour/<int:id>/', views.tourView),
    path('departure/<str:departure>/', views.departureView),
]
