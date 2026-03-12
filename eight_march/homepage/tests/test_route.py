from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from homepage.models import Postcard, Recepient


class TestHomePage(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Подготовка данных для тестов."""
        cls.recepient = Recepient.objects.create(
            name='Получатель',
            slug='recepient',
        )
        cls.image = Postcard.objects.create(
            recepient=cls.recepient,
            path_image='media/postcards/first.png',
        )

    def test_pages_availability_for_anonymous(self):
        """Тестирование доступа страниц анонимным пользователям."""
        urls = (
            reverse('home:index'),
            reverse('home:album', args=(self.recepient.slug,)),
        )
        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)
