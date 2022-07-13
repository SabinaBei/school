# Generated by Django 4.0.6 on 2022-07-13 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('duration', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_active', models.BooleanField(default=True)),
                ('id_school', models.CharField(max_length=155, null=True)),
                ('max_students', models.DecimalField(decimal_places=0, max_digits=2, null=True)),
                ('type_of_education', models.CharField(max_length=155, null=True)),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'duration', 'price')},
            },
        ),
    ]
