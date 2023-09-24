from http import HTTPStatus

from django.test import TestCase


class UrlsTests(TestCase):

    def test_unknown_page_return_404(self) -> None:
        """Неизвестная страница возвращает 404."""

        self.assertEqual(self.client.get('/test666/').status_code, HTTPStatus.NOT_FOUND)

    def test_all_urls_available(self) -> None:
        """Все адреса доступны."""

        self.assertEqual(self.client.get('/admin/').status_code, HTTPStatus.FOUND)
        self.assertEqual(self.client.get('/api/v1/upload/').status_code, HTTPStatus.METHOD_NOT_ALLOWED)
        self.assertEqual(self.client.get('/api/v1/files/').status_code, HTTPStatus.OK)
