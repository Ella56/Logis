# Generated by Django 5.1.4 on 2024-12-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(default='default.jpg', upload_to='service')),
                ('desc', models.TextField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('contact', models.CharField(max_length=120)),
                ('image', models.ImageField(default='default.jpg', upload_to='service')),
                ('status', models.BooleanField(default=True)),
                ('options', models.ManyToManyField(to='services.options')),
            ],
        ),
        migrations.CreateModel(
            name='Services_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.CharField(max_length=120)),
                ('desc', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='service')),
                ('status', models.BooleanField(default=True)),
                ('category', models.ManyToManyField(to='services.category')),
                ('options', models.ManyToManyField(to='services.options')),
            ],
        ),
    ]
