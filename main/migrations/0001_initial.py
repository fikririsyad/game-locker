# Generated by Django 4.2.5 on 2023-09-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('genre', models.CharField(max_length=30)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
