from django.contrib import admin
from django.urls import path, include
from .views import SongHomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', include('lyric.urls', namespace='lyric')),
    path('', SongHomeView.as_view(), name='home')
]
