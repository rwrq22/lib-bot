# Generated by Django 4.2.1 on 2023-06-22 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'permissions': [('delete_yourmodel', 'Can delete YourModel')]},
        ),
    ]