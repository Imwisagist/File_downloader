import sys
from io import StringIO

from django.test import TestCase

from ..models import File


class SignalsTests(TestCase):

    def test_signal_works_correct(self) -> None:
        """Сигнал отправляет файл в обработку при создании."""

        buffer = StringIO()
        original_std = sys.stdout
        sys.stdout = buffer

        File.objects.create(file='tests/fixtures/Screenshot_for_test.png')

        output = buffer.getvalue().strip()

        self.assertEqual(output, 'tests/fixtures/Screenshot_for_test.png - отправлен в обработку')

        sys.stdout = original_std
