# Generated by Django 4.2.3 on 2023-07-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0002_alter_temp_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='mobile'),
        ),
    ]
