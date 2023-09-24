import sys
from io import StringIO

from django.test import TestCase

from ..models import File
from ..tasks import process_image, process_text, process_other_type


class ViewsTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.file_obj = File.objects.create(
            file='tests/fixtures/Screenshot_for_test.png'
        )
        cls.file_obj2 = File.objects.create(
            file='tests/fixtures/mu_secret_passwords.txt'
        )
        cls.file_obj3 = File.objects.create(
            file='tests/fixtures/hard_work.docx'
        )

    def test_process_image_works_correct(self) -> None:
        """Задача по обработке изображений успешно проходит."""

        buffer = StringIO()
        original_std = sys.stdout
        sys.stdout = buffer

        process_image(self.file_obj.pk)

        output = buffer.getvalue().strip()

        self.assertEqual(output, f'{self.file_obj.file.name} - успешно обработан')

        sys.stdout = original_std

    def test_process_text_works_correct(self) -> None:
        """Задача по обработке текста успешно проходит."""

        buffer = StringIO()
        original_std = sys.stdout
        sys.stdout = buffer

        process_text(self.file_obj2.pk)

        output = buffer.getvalue().strip()

        self.assertEqual(output, f'{self.file_obj2.file.name} - успешно обработан')

        sys.stdout = original_std

    def test_process_other_type_works_correct(self) -> None:
        """Задача по обработке других типов успешно проходит."""

        buffer = StringIO()
        original_std = sys.stdout
        sys.stdout = buffer

        process_other_type(self.file_obj3.pk)

        output = buffer.getvalue().strip()

        self.assertEqual(output, f'{self.file_obj3.file.name} - успешно обработан')

        sys.stdout = original_std
