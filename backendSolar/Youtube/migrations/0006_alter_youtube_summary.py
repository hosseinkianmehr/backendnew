# Generated by Django 3.2.7 on 2022-02-21 20:57

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Youtube', '0005_youtube_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='Summary',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
