# Generated by Django 4.0.4 on 2022-07-11 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_crm', '0006_remove_stages_link_stages_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('status_sales', models.CharField(max_length=50)),
                ('status_competitors', models.CharField(max_length=50)),
                ('additionally', models.TextField(max_length=500)),
            ],
        ),
        migrations.AlterModelOptions(
            name='stages',
            options={'verbose_name': 'Этап продажы', 'verbose_name_plural': 'Этапы продаж'},
        ),
    ]
