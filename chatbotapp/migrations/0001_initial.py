# Generated by Django 3.2.11 on 2022-01-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChaSeDae',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moms', models.TextField(null=True, verbose_name='맘스')),
                ('chef', models.TextField(null=True, verbose_name='셰프')),
                ('special', models.TextField(null=True, verbose_name='정찬')),
                ('salad', models.TextField(null=True, verbose_name='샐러드')),
                ('dinner', models.TextField(null=True, verbose_name='석식')),
                ('takeOut', models.TextField(null=True, verbose_name='TakeOut')),
                ('date', models.DateField(null=True, verbose_name='날짜')),
            ],
        ),
        migrations.CreateModel(
            name='Nano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunchA', models.TextField(null=True, verbose_name='코스A')),
                ('lunchB', models.TextField(null=True, verbose_name='코스B')),
                ('plus', models.TextField(null=True, verbose_name='PLUS')),
                ('dinner', models.TextField(null=True, verbose_name='저녁')),
                ('date', models.DateField(null=True, verbose_name='날짜')),
            ],
        ),
        migrations.CreateModel(
            name='RDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korea', models.TextField(null=True, verbose_name='한식')),
                ('special', models.TextField(null=True, verbose_name='일품')),
                ('lunch_plus', models.TextField(null=True, verbose_name='점심 플러스바')),
                ('dinner', models.TextField(null=True, verbose_name='저녁')),
                ('dinner_plus', models.TextField(null=True, verbose_name='저녁 플러스바')),
                ('takeOut', models.TextField(null=True, verbose_name='TakeOut')),
                ('date', models.DateField(null=True, verbose_name='날짜')),
            ],
        ),
    ]
