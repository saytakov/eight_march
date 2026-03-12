from typing import Any

from django.db.models.query import QuerySet
from django.views.generic import ListView, TemplateView

from .models import Postcard, Recepient


class IndexTemplateView(TemplateView):
    """CBV для главной страницы."""
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        """Добавление в контекст получаетелей из БД."""
        context = super().get_context_data(**kwargs)
        context["recepients"] = Recepient.objects.all()
        return context


class AlbumListView(ListView):
    """CBV для страницы с открытками конкретного получателя."""
    template_name = 'homepage/album.html'

    def get_queryset(self) -> QuerySet[Any]:
        """Выборка открыток по слагу пользователя."""
        return Postcard.objects.filter(recepient__slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs: Any):
        """Добавление в конекст информации о получаетеле из бд."""
        context = super().get_context_data(**kwargs)
        context['person'] = Recepient.objects.get(slug=self.kwargs.get('slug'))
        return context
