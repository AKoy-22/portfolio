# Generated by Django 4.2.1 on 2023-08-16 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_weblinkg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='weblinkg',
            new_name='weblink',
        ),
    ]