# Generated by Django 4.2.4 on 2024-03-16 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_ad_address_delete_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.category'),
        ),
    ]
