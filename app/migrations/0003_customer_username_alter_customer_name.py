# Generated by Django 4.0.5 on 2022-06-17 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='userName',
            field=models.CharField(default=1, max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
