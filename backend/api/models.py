from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models


class File(models.Model):
    """
    The model describing the file,
    the date and time it was uploaded, 
    and whether the file was processed.
    """

    file = models.FileField(
        'Загруженный файл',
        upload_to='uploaded_files/',
        validators=(FileExtensionValidator(settings.ALLOWED_EXTENTIONS),)
    )
    uploaded_at = models.DateTimeField(
        'Дата и время загрузки',
        auto_now_add=True,
    )
    processed = models.BooleanField(
        'Флаг обработки',
        default=False,
    )

    def __str__(self):
        return f'Файл с id - {self.pk}'

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
