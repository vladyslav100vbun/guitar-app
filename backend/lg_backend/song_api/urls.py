from django.urls import path
from .views import SongListView, SongDetailView, GenreListView

urlpatterns = [
    path('songs/', SongListView.as_view(), name='song-list'),
    path('songs/<slug:slug>/', SongDetailView.as_view(), name='song-detail'),
    path('genres/', GenreListView.as_view(), name='genres'),
]