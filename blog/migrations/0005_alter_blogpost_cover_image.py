# Generated by Django 4.0.5 on 2022-06-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogpost_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='cover_image',
            field=models.ImageField(default='cool.jpg', upload_to=''),
        ),
    ]
