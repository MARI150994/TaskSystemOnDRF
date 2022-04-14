# Generated by Django 3.1 on 2022-04-13 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Name of task')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('status', models.CharField(blank=True, choices=[('In work', 'In work'), ('Canceled', 'Canceled'), ('Finished', 'Finished'), ('Awaiting', 'Awaiting')], max_length=40, verbose_name='Status of project/task')),
                ('priority', models.CharField(choices=[('Very high', 'Very important'), ('High', 'High'), ('Middle', 'Middle'), ('Low', 'Low'), ('Very low', 'Very low')], max_length=40, verbose_name='Priority of project/task')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Time when project/task was created')),
                ('planned_date', models.DateTimeField(verbose_name='Planned end date')),
                ('finish_date', models.DateTimeField(blank=True, null=True, verbose_name='Time when project/task was finished')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Users hwo can delegate and update')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Name of task')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('status', models.CharField(blank=True, choices=[('In work', 'In work'), ('Canceled', 'Canceled'), ('Finished', 'Finished'), ('Awaiting', 'Awaiting')], max_length=40, verbose_name='Status of project/task')),
                ('priority', models.CharField(choices=[('Very high', 'Very important'), ('High', 'High'), ('Middle', 'Middle'), ('Low', 'Low'), ('Very low', 'Very low')], max_length=40, verbose_name='Priority of project/task')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Time when project/task was created')),
                ('planned_date', models.DateTimeField(verbose_name='Planned end date')),
                ('finish_date', models.DateTimeField(blank=True, null=True, verbose_name='Time when project/task was finished')),
                ('start_await_date', models.DateTimeField(blank=True, null=True)),
                ('active_time', models.DurationField(blank=True, null=True)),
                ('passive_time', models.DurationField(blank=True, null=True)),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Executor of this task')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='task.task')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='task.project')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]
