# Generated by Django 4.2.6 on 2023-10-24 21:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0003_alter_conversationmessage_conversation'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
