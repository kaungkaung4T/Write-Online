# Generated by Django 3.2.9 on 2022-07-15 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0005_write_folder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='write',
            old_name='folder',
            new_name='folder_page',
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder', models.CharField(max_length=225)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('write', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='display.write')),
            ],
        ),
    ]
