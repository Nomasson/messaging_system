# Generated by Django 3.2.3 on 2021-06-01 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Message', '0002_message_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(max_length=250),
        ),
    ]
