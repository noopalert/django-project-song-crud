from typing import Any
from django.views.generic import TemplateView
from lyric.views import SongGenre


class SongHomeView(TemplateView, SongGenre):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any):
        queryset = self.get_latest_song()
        context={
            'latest_song_list': queryset
        }    
        return context

