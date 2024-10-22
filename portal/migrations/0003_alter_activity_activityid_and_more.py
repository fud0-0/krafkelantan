# Generated by Django 5.1.2 on 2024-10-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_remove_activity_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activityID',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='performance',
            name='performanceID',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stall',
            name='stallID',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]