# Generated by Django 4.0.4 on 2022-04-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ustoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('familiya', models.CharField(max_length=30)),
                ('daraja', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
