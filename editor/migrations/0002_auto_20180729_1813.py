# Generated by Django 2.0 on 2018-07-29 09:13

from django.db import migrations
import django.utils.timezone
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memo',
            old_name='update_time',
            new_name='modify_time',
        ),
        migrations.AddField(
            model_name='memo',
            name='content',
            field=markdownx.models.MarkdownxField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
