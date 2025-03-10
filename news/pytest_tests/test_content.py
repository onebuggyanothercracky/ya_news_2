import pytest
from django.conf import settings
from django.urls import reverse


@pytest.mark.django_db
def test_note_in_list_for_author(news_20, client):
    url = reverse('news:home')

    response = client.get(url)

    object_list = response.context['object_list']
    news_count = object_list.count()

    assert news_count == 10


