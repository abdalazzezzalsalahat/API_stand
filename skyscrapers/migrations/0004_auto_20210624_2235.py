# Generated by Django 3.1.7 on 2021-06-24 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skyscrapers', '0003_alter_skyscraper_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skyscraper',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
