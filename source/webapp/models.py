from django.db import models
from django.utils import timezone

DEFAULT_CATEGORY = 'active'

STATUS_CHOICES = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано'),
]


class Review(models.Model):
    author = models.CharField(max_length=40, null=False, blank=False, default='Unknown', verbose_name='Автор')
    email = models.EmailField(max_length=40, null=False, blank=False, default='Unknown', verbose_name='Автор')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    category = models.CharField(max_length=20, default=DEFAULT_CATEGORY, choices=CATEGORY_CHOICES, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

