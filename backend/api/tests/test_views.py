import shutil
import tempfile
from http import HTTPStatus

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from rest_framework.serializers import ListSerializer

from ..models import File

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR.parent / 'uploaded_files')


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class ViewsTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.small_jpg = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B'
        )
        cls.uploaded = SimpleUploadedFile(
            name='small.jpg',
            content=cls.small_jpg,
            content_type='image/jpg'
        )
        cls.file_obj = File.objects.create(
            file='tests/fixtures/Screenshot_for_test.png'
        )
        cls.file_obj2 = File.objects.create(
            file='tests/fixtures/Screenshot_for_test.png'
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Удаление временных файлов после тестов."""
        super().tearDownClass()
        shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)

    def test_endpoint_files_works_correct(self) -> None:
        """Эндпоинт files/ возвращает список файлов."""

        self.assertEqual(File.objects.count(), 2)
        self.assertIsInstance(self.client.get('/api/v1/files/').data['results'].serializer, ListSerializer)
        self.assertEqual(self.client.get('/api/v1/files/').data['count'], 2)

    def test_endpoint_upload_works_correct(self) -> None:
        """Эндпоинт upload/ загружает переданный файл, а processed автоматически устанавливается в False."""

        self.assertEqual(File.objects.count(), 2)

        response = self.client.post('/api/v1/upload/', {'file': self.uploaded}, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

        self.assertEqual(File.objects.count(), 3)

        self.assertEqual(File.objects.last().processed, False)
