from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone

class Lyric(models.Model):
    title = models.CharField(max_length=255)
    lyrics = models.TextField()
    genre = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(null=True)
    published = models.DateTimeField(null=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        if self.is_published == True:
            self.published = timezone.now()
        else:
            self.published = None
        super().save()

    def get_absolute_url(self):
        url_slug = {'slug': self.slug}
        return reverse('lyric:detail', kwargs=url_slug)
    

    def __str__(self):
        return '{}. {} - {}'.format(self.id, self.title, self.artist)