# Generated by Django 3.2.7 on 2021-12-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TagAndComment', '0001_initial'),
        ('Youtube', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtube',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tagsYoutube', to='TagAndComment.tag', verbose_name='tagyoutube'),
        ),
    ]
