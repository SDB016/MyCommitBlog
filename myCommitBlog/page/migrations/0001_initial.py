# Generated by Django 3.2.5 on 2021-08-01 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('writer', models.CharField(max_length=20)),
                ('createdDate', models.DateTimeField()),
                ('updatedDate', models.DateTimeField()),
            ],
        ),
    ]
