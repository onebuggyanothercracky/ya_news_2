import unittest

from django.test import TestCase

from news.models import News

@unittest.skip('Пропускаем')
class TestNews(TestCase): 

    
    @classmethod
    def setUpTestData(cls):
        cls.news = News.objects.create(
            title='Заголовок новости',
            text='Тестовый текст',
        )

    def test_successful_creation(self):
        news_count = News.objects.count()
        self.assertEqual(news_count, 1)

    def test_title(self):
        # Сравним свойство объекта и ожидаемое значение.
        self.assertEqual(self.news.title, 'Заголовок новости')
