# Generated by Django 4.2.4 on 2024-03-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_ad_slugify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='address',
            field=models.CharField(max_length=55),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]