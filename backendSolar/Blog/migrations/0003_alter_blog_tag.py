# Generated by Django 3.2.7 on 2021-12-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TagAndComment', '0001_initial'),
        ('Blog', '0002_blog_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tagsBlog', to='TagAndComment.tag', verbose_name='tagblog'),
        ),
    ]
