# Generated by Django 3.2.7 on 2022-04-16 09:04

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_auto_20220222_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='content1',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content10',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content3',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content4',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content5',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content6',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content7',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content8',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content9',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge1',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge10',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge1010',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge11',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge2',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge22',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge3',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge33',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge4',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge44',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge5',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge55',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge6',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge66',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge7',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge77',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge8',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge88',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge9',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='iamge99',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='titel',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='titel'),
        ),
        migrations.AddField(
            model_name='blog',
            name='titel1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='titel'),
        ),
        migrations.AddField(
            model_name='blog',
            name='titel2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='titel'),
        ),
        migrations.AddField(
            model_name='blog',
            name='titel3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='titel'),
        ),
        migrations.DeleteModel(
            name='content',
        ),
    ]
