import pytest
from http import HTTPStatus
from pytest_django.asserts import assertRedirects
from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name, arg',
    (
        ('news:home', None),
        ('users:login', None),
        ('users:logout', None),
        ('users:signup', None),
        ('news:detail', pytest.lazy_fixture('id_for_news')),
    )
)
def test_pages_availability_for_anonymous_user(client, name, arg):
    url = reverse(name, args=arg)
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK

@pytest.mark.django_db
@pytest.mark.parametrize(
    'parametrized_client, expected_status',
    (
        (pytest.lazy_fixture('not_author_client'), HTTPStatus.NOT_FOUND),
        (pytest.lazy_fixture('author_client'), HTTPStatus.OK)
    ),
)
@pytest.mark.parametrize(
    'name',
    ('news:edit', 'news:delete',)
)
def test_edit_or_delete_news_by_author(
    parametrized_client,
    expected_status,
    comment,
    name,
):
    url = reverse(name, args=(comment.id,))
    response = parametrized_client.get(url)
    assert response.status_code == expected_status

@pytest.mark.django_db
@pytest.mark.parametrize(
    'name, arg',
    (
        ('news:edit', pytest.lazy_fixture('id_for_news')),
        ('news:delete', pytest.lazy_fixture('id_for_news')),
    ),
)
def test_redirects(client, name, arg):
    login_url = reverse('users:login')
    url = reverse(name, args=arg)
    expected_url = f'{login_url}?next={url}'
    response = client.get(url)
    assertRedirects(response, expected_url)
