# Generated by Django 4.2.1 on 2023-08-29 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_rename_weblinkg_post_weblink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='weblink',
            field=models.URLField(blank=True, null=True),
        ),
    ]