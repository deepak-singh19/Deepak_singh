# Generated by Django 2.1.5 on 2020-01-16 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deepak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('role', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('isActive', models.CharField(max_length=100)),
                ('_created_at', models.IntegerField()),
                ('_uploaded_at', models.IntegerField()),
            ],
        ),
    ]
