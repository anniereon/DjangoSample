# Generated by Django 5.2.1 on 2025-06-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_racedetail_check_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racedetail',
            name='rank',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
