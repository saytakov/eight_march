from django.urls import path
from homepage import views

app_name = 'home'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('album/<slug:slug>/', views.AlbumListView.as_view(), name='album'),
]
