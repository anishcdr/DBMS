# Generated by Django 4.2.4 on 2024-03-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_fixture_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='Round_number',
            field=models.CharField(max_length=10),
        ),
    ]
