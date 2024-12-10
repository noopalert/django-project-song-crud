from django.urls import path,re_path
from .views import (
    LyricListView,
    LyricDetailView,
    LyricGenreListView,
    LyricCreateView,
    LyricManageView,
    LyricDeleteView,
    LyricUpdateView
)

app_name = 'lyric'

urlpatterns = [
    re_path(r'^(?P<page>\d+)$', LyricListView.as_view(), name='list'),
    re_path(r'^detail/(?P<slug>[\w-]+)$', LyricDetailView.as_view(), name='detail'),
    re_path(r'^genre/(?P<genre>[\w]+)/(?P<page>\d+)$', LyricGenreListView.as_view(), name='genre'),
    path('create/', LyricCreateView.as_view(), name='create'),
    path('manage/', LyricManageView.as_view(), name='manage'),
    re_path(r'^manage/delete/(?P<pk>\d+)$', LyricDeleteView.as_view(), name='delete'),
    re_path(r'^manage/update/(?P<pk>\d+)$', LyricUpdateView.as_view(), name='update'),
]