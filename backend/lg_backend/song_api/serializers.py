from rest_framework import serializers
from .models import Song, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'slug']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'photo', 'difficulty_level', 'genre', 'tablature_photo', 'video_link', 'slug']
