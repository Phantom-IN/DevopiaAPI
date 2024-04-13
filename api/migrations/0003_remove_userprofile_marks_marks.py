# Generated by Django 5.0.2 on 2024-04-13 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_userprofile_marks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='marks',
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(default=0)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile')),
            ],
            options={
                'unique_together': {('user', 'subject')},
            },
        ),
    ]