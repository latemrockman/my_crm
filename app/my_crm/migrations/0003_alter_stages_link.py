# Generated by Django 4.0.4 on 2022-07-11 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_crm', '0002_stages_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stages',
            name='link',
            field=models.CharField(default='a', max_length=20),
        ),
    ]
