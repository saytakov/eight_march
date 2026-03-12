"""Модуль для тестирования содержимого на страницах."""
from django.test import TestCase
from django.urls import reverse
from homepage.models import Postcard, Recepient


class TestHomePage(TestCase):

    def test_recepients_in_context(self):
        """Проверка на наличие получателей на главной странице."""
        url = reverse('home:index')
        resposne = self.client.get(url)
        self.assertIn('recepients', resposne.context)


class TestAlbumPage(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Подготовка данных для тестов."""
        cls.recepient = Recepient.objects.create(
            name='Получатель',
            slug='recepient'
        )
        cls.image = Postcard.objects.create(
            recepient=cls.recepient,
            path_image='media/postcards/first.png',
        )

    def test_query_set_in_context(self):
        """Проверка на наличие открыток в контексте."""
        url = reverse('home:album', args=(self.recepient.slug,))
        response = self.client.get(url)
        self.assertIn('object_list', response.context)
        self.assertEqual(response.context['object_list'].count(), 1)

    def test_person_in_context(self):
        """
        Проверка на наличие получателя в контексте,
        на странице с альбомом.
        """
        url = reverse('home:album', args=(self.recepient.slug,))
        response = self.client.get(url)
        self.assertIn('person', response.context)
        person = response.context['person']
        self.assertEqual(person.name, self.recepient.name)
