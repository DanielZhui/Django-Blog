# Generated by Django 2.2.3 on 2020-06-26 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-createdAt'], 'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
    ]
