# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('vin', models.CharField(unique=True, max_length=50)),
                ('number', models.CharField(max_length=10)),
                ('brand', models.CharField(max_length=40)),
                ('model', models.CharField(max_length=40)),
                ('year', models.IntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)], max_length=4, default=2016)),
                ('engine', models.FloatField()),
                ('horsepower', models.IntegerField()),
                ('transmission', models.CharField(choices=[('Aвтомат', 'Автоматическая'), ('Mеханика', 'Механическая')], max_length=20, default='Не выбрано')),
                ('gearing', models.CharField(choices=[('Передний', 'Передний'), ('Задний', 'Задний'), ('Полный', 'Полный')], max_length=20, default='Не выбрано')),
                ('fuel', models.CharField(choices=[('Бензин АИ-80', 'Бензин АИ-80'), ('Бензин АИ-92', 'Бензин АИ-92'), ('Бензин АИ-95', 'Бензин АИ-95'), ('Бензин АИ-98', 'Бензин АИ-98'), ('Дизельное топливо', 'Дизельное топливо'), ('ГАЗ', 'ГАЗ')], max_length=30, default='Не выбрано')),
                ('mileage', models.IntegerField()),
                ('body', models.CharField(choices=[('Седан', 'Седан'), ('Универсал', 'Универсал'), ('Хетчбэк', 'Хетчбэк'), ('Купе', 'Купе'), ('Минивэн', 'Минивэн'), ('Пикап', 'Пикап'), ('Фургон', 'Фургон'), ('Кабриолет', 'Кабриолет'), ('Микроавтобус', 'Микроавтобус'), ('Лимузин', 'Лимузин')], max_length=20, default='Не выбрано')),
                ('color', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to='', blank=True)),
                ('sell', models.BooleanField()),
                ('notes', models.IntegerField()),
                ('owner_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Car',
            },
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('what', models.CharField(max_length=1000)),
                ('when', models.DateField()),
                ('price', models.FloatField(max_length=20)),
                ('car_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Cost',
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('header', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=3000)),
                ('date', models.DateField()),
                ('car_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Mark',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('header', models.CharField(max_length=100)),
                ('business', models.CharField(max_length=500)),
                ('time', models.DateField()),
                ('done', models.BooleanField()),
                ('car_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Notification',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('who', models.CharField(max_length=100)),
                ('what', models.CharField(max_length=1000)),
                ('details', models.CharField(max_length=100)),
                ('when', models.DateField()),
                ('price', models.FloatField()),
                ('reserve', models.IntegerField()),
                ('car_id', models.IntegerField()),
                ('start_mileage', models.IntegerField()),
            ],
            options={
                'db_table': 'Service',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
