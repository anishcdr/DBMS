# Generated by Django 4.2.4 on 2024-03-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_fixture_icc_ranking_login_results_delete_soildata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='Date',
            field=models.CharField(max_length=10),
        ),
    ]
