# Generated by Django 4.1.7 on 2023-03-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_blog_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='summary',
            field=models.TextField(blank=True, max_length=30),
        ),
    ]
