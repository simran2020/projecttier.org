# Generated by Django 2.1.8 on 2019-05-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_remove_person_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='personcategory',
            name='tier_title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]