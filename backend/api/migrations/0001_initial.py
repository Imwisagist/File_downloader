import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploaded_files/', validators=[django.core.validators.FileExtensionValidator(('jpg', 'jpeg', 'png', 'txt', 'docx'))], verbose_name='Загруженный файл')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время загрузки')),
                ('processed', models.BooleanField(default=False, verbose_name='Флаг обработки')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]
