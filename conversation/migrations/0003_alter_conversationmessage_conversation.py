# Generated by Django 4.2.6 on 2023-10-24 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0002_rename_cocnversation_conversationmessage_conversation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationmessage',
            name='conversation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='conversation.conversation'),
        ),
    ]