# Generated by Django 4.0.4 on 2022-07-11 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_crm', '0003_alter_stages_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='stages',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
