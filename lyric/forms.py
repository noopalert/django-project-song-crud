from django.forms import ModelForm
from .models import Lyric

class LyricForm(ModelForm):
    class Meta:
        model = Lyric
        fields=[
            'title',
            'lyrics',
            'genre',
            'artist',
        ]