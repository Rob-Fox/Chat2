# Generated by Django 2.1.3 on 2018-11-16 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('Created_At', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
