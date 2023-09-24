from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import File
from .tasks import process_image, process_other_type, process_text


@receiver(post_save, sender=File)
def handle_uploaded_file(sender, instance, created, **kwargs):
    """
    This handler is needed to transfer it to the correct 
    сelery handler for processing, depending on the file extension.
    """

    if created:
        extention: str = instance.file.name.split('.')[-1]
        print(f'{instance.file.name} - отправлен в обработку')

        if extention in settings.ALLOWED_IMAGE_EXTENTIONS:
            process_image.delay(instance.pk)
        elif extention in settings.ALLOWED_TEXT_EXTENTIONS:
            process_text.delay(instance.pk)
        else:
            process_other_type.delay(instance.pk)