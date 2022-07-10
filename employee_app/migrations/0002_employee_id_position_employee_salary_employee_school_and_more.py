# Generated by Django 4.0.6 on 2022-07-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='id_position',
            field=models.CharField(max_length=155, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='school',
            field=models.CharField(max_length=155, null=True),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('duration', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=255)),
                ('permission', models.CharField(max_length=155)),
                ('id_department', models.CharField(max_length=155)),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'duration', 'description', 'permission')},
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('duration', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'duration', 'description')},
            },
        ),
    ]
