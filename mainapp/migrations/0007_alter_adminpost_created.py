# Generated by Django 5.1.2 on 2024-11-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_topictheme_dktopic_topictheme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpost',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
