# Generated by Django 2.2.7 on 2019-12-16 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='Date: ')),
                ('article', models.CharField(max_length=200)),
                ('content', models.TextField(default='')),
                ('likes', models.IntegerField(default=0)),
                ('category', models.ManyToManyField(to='home.Category')),
                ('country', models.ManyToManyField(to='home.Country')),
            ],
        ),
    ]
