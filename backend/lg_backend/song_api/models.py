from django.db import models
from django.utils.text import slugify


class Genre(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Song(models.Model):
    LEVEL_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    GENRE_CHOICES = [
        ('rock', 'Rock'),
        ('pop', 'Pop'),
        ('hip-hop', 'Hip Hop'),
    ]

    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    difficulty_level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES)
    tablature_photo = models.ImageField(upload_to='tablature_photos/', null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
