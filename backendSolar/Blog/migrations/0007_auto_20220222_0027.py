# Generated by Django 3.2.7 on 2022-02-21 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_alter_blog_content1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='titel',
        ),
        migrations.AddField(
            model_name='blog',
            name='main_titel',
            field=models.CharField(default='null', max_length=50, verbose_name='titel'),
        ),
        migrations.AddField(
            model_name='blog',
            name='titel1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='titel'),
        ),
    ]