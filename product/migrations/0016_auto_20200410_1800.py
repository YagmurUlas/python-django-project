# Generated by Django 3.0.3 on 2020-04-10 15:00

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_activity_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]