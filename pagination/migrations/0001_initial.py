# Generated by Django 3.0 on 2019-12-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('start', models.IntegerField(default=0)),
                ('end', models.IntegerField(default=1)),
                ('total_obj', models.IntegerField()),
            ],
        ),
    ]
