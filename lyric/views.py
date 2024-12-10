from typing import Any
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from .models import Lyric
from .forms import LyricForm

class SongGenre():
    model = Lyric
    
    def get_latest_song(self):
        listGenre = self.model.objects.values_list('genre', flat=True).distinct()
        queryset = []

        for genre in listGenre:
            lyric = self.model.objects.filter(genre=genre).latest('published')
            queryset.append(lyric)
        
        return queryset

class LyricGenreListView(ListView):
    model = Lyric
    template_name = 'lyric/lyric_genre_list.html'
    ordering = ['-published']
    context_object_name = 'lyric_list'
    paginate_by = 2

    def get_queryset(self):
        self.queryset = self.model.objects.filter(genre = self.kwargs['genre'])
        return super().get_queryset()
    
    def get_context_data(self, *args, **kwargs):
        listGenre = self.model.objects.values_list('genre', flat=True).distinct().exclude(genre=self.kwargs['genre'])
        self.kwargs.update({
            'listGenre': listGenre
        })
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

class LyricListView(ListView):
    model = Lyric
    template_name = 'lyric/lyric_list.html'
    context_object_name = 'lyric_list'
    ordering = ['-published']
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        listGenre = self.model.objects.values_list('genre', flat=True).distinct()
        self.kwargs.update({
            'listGenre': listGenre
        })
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

class LyricDetailView(DetailView):
    model = Lyric
    template_name = 'lyric/lyric_detail.html'
    context_object_name = 'lyric'

    def get_context_data(self, *args, **kwargs):
        listGenre = self.model.objects.values_list('genre', flat=True).distinct()
        relatedSong = self.model.objects.filter(genre=self.object.genre).exclude(id=self.object.id)
        self.kwargs.update({
            'listGenre': listGenre,
            'relatedSong': relatedSong,
        })
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
    
class LyricCreateView(CreateView):
    form_class = LyricForm
    template_name = 'lyric/lyric_create.html'

class LyricManageView(ListView):
    model = Lyric
    template_name = 'lyric/lyric_manage.html'
    context_object_name = 'lyric_list'

class LyricDeleteView(DeleteView):
    model = Lyric
    template_name = 'lyric/lyric_delete_confirmation.html'
    success_url = reverse_lazy('lyric:manage')

class LyricUpdateView(UpdateView):
    model = Lyric
    form_class = LyricForm
    template_name = 'lyric/lyric_update.html'
