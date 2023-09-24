from celery import shared_task
from django.shortcuts import get_object_or_404

from .models import File


@shared_task()
def process_image(file_pk: int) -> None:
    try:
        file_instance: File | None = get_object_or_404(File, pk=file_pk)
        file_instance.processed = True
        file_instance.save()
    except Exception as err:
        print(f'Не удалось обработать файл. Ошибка - {err}')
    else:
        print(f'{file_instance.file.name} - успешно обработан')


@shared_task()
def process_text(file_pk: int) -> None:
    try:
        file_instance: File | None = get_object_or_404(File, pk=file_pk)
        file_instance.processed = True
        file_instance.save()
    except Exception as err:
        print(f'Не удалось обработать файл. Ошибка - {err}')
    else:
        print(f'{file_instance.file.name} - успешно обработан')


@shared_task()
def process_other_type(file_pk: int) -> None:
    try:
        file_instance: File | None = get_object_or_404(File, pk=file_pk)
        file_instance.processed = True
        file_instance.save()
    except Exception as err:
        print(f'Не удалось обработать файл. Ошибка - {err}')
    else:
        print(f'{file_instance.file.name} - успешно обработан')
