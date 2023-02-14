from django.urls import path
from games.api import views as api_views

urlpatterns = [
    path('developer/',api_views.DeveloperListCreateAPIView.as_view(), name='developer-list'),
    path('developer/<int:pk>', api_views.DeveloperDetailAPIView.as_view(), name='developer-detail'),

    path('game/',api_views.GameListCreateAPIView.as_view(), name='game-list'),
    path('game/<int:pk>', api_views.GameDetailAPIView.as_view(), name='game-detail'),
    
]




