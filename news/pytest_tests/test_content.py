import pytest
from django.conf import settings
from django.urls import reverse

from news.forms import CommentForm


@pytest.mark.django_db
def test_news_in_list(news_20, client):
    url = reverse('news:home')

    response = client.get(url)

    object_list = response.context['object_list']
    news_count = object_list.count()

    assert news_count == 10


@pytest.mark.django_db
def test_order_news_in_list(news_20, client):
    url = reverse('news:home')

    response = client.get(url)

    object_list = response.context['object_list']
    all_dates = [news.date for news in object_list]
    sorted_dates = sorted(all_dates, reverse=True)

    assert all_dates == sorted_dates


@pytest.mark.django_db
def test_news_page_contains_form(id_for_news, author_client):
    url = reverse('news:detail', args=id_for_news)
    response = author_client.get(url)
    assert 'form' in response.context
    # Проверяем, что объект формы относится к нужному классу.
    assert isinstance(response.context['form'], CommentForm)
