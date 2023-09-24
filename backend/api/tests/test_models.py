from django.conf import settings
from django.test import TestCase

from ..models import File


class ModelsTests(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.file_obj = File.objects.create(
            file='tests/fixtures/Screenshot_for_test.png'
        )

    def test_model_file_fields_have_correct_verboses(self) -> None:
        """Все поля модели File имеют корректные verbose_name."""

        file_fields_and_expectations = (
            ('file', 'Загруженный файл'),
            ('uploaded_at', 'Дата и время загрузки'),
            ('processed', 'Флаг обработки'),
        )

        for field, expectation in file_fields_and_expectations:
            with self.subTest(field=field):
                self.assertEqual(
                    self.file_obj._meta.get_field(field).verbose_name, expectation
                )

    def test_model_file_fields_have_correct_str_and_meta_verboses(self) -> None:
        """Модель File имеет корректные str and meta_verboses."""

        file_fields_and_expectations = (
            (self.file_obj._meta.verbose_name, 'Файл'),
            (self.file_obj._meta.verbose_name_plural, 'Файлы'),
            (str(self.file_obj), f'Файл с id - {self.file_obj.pk}'),
        )

        for field, expectation in file_fields_and_expectations:
            with self.subTest(field=field):
                self.assertEqual(field, expectation)

    def test_model_file_fields_have_correct_arguments(self) -> None:
        """Все поля модели File имеют корректные аргументы."""

        file_fields_and_expectations = (
            (self.file_obj._meta.get_field('file').upload_to, 'uploaded_files/'),
            (self.file_obj._meta.get_field('file').validators[0].allowed_extensions, list(settings.ALLOWED_EXTENTIONS)),
            (self.file_obj._meta.get_field('uploaded_at').auto_now_add, True),
            (self.file_obj._meta.get_field('processed').default, False),
        )

        for field, expectation in file_fields_and_expectations:
            with self.subTest(field=field):
                self.assertEqual(field, expectation)

    def test_method_save_works_correct(self) -> None:
        """Проверка сохранения экземпляра в базу."""

        self.assertTrue(File.objects.filter(file='tests/fixtures/Screenshot_for_test.png').exists())
