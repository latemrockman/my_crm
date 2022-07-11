# Generated by Django 4.0.4 on 2022-07-11 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_crm', '0007_clients_alter_stages_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterField(
            model_name='clients',
            name='status_sales',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='my_crm.stages'),
        ),
    ]
