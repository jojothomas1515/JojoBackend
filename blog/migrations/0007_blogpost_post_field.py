# Generated by Django 4.0.5 on 2022-07-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_field',
            field=models.TextField(blank=True, null=True),
        ),
    ]
