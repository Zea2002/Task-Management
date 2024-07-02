# Generated by Django 5.0.6 on 2024-07-02 10:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=200)),
                ('taskDescription', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('taskAssignDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('categories', models.ManyToManyField(to='category.taskcategory')),
            ],
        ),
    ]
