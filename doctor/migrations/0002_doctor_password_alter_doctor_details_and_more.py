# Generated by Django 4.2.5 on 2023-09-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='details',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='location',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(default='', upload_to='doctors'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='price_range',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='qualification',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='rating',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='tags',
            field=models.CharField(default='', max_length=100),
        ),
    ]
