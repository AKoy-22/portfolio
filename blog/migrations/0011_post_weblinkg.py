# Generated by Django 4.2.1 on 2023-08-16 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='weblinkg',
            field=models.URLField(null=True),
        ),
    ]
