# Generated by Django 3.0.5 on 2020-05-10 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]