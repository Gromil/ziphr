# Generated by Django 3.1.4 on 2022-08-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0002_auto_20220827_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airplane',
            name='plane_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
