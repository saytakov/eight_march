from django.db import models


class Recepient(models.Model):
    """Модель получателей открыток."""

    name = models.TextField(
        max_length=32,
        verbose_name='Имя получателя'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Слаг получателя',
    )

    class Meta:
        verbose_name: str = 'получатель'
        verbose_name_plural: str = 'Получатели'

    def __str__(self) -> str:
        return self.slug


class Postcard(models.Model):
    """Модель с открытками."""

    recepient = models.ForeignKey(
        Recepient,
        on_delete=models.CASCADE,
    )
    path_image = models.ImageField(
        verbose_name='Фотография',
        upload_to='postcards',
        blank=True,
    )
    description = models.TextField(
        'Описание',
        max_length=256,
    )

    class Meta:
        verbose_name: str = 'Открытка'
        verbose_name_plural: str = 'Открытки'

    def __str__(self) -> str:
        return self.description
