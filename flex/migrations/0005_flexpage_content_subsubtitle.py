# Generated by Django 3.0.3 on 2022-01-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0004_auto_20220104_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='content_subSubtitle',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
