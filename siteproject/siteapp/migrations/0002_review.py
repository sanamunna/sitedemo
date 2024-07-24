# Generated by Django 4.1.4 on 2022-12-31 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('imgs', models.ImageField(upload_to='pics')),
                ('descr', models.TextField()),
            ],
        ),
    ]