# Generated by Django 4.0.6 on 2022-07-11 10:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee_app', '0006_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together={('user', 'date_of_birth', 'phone_number')},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
    ]
