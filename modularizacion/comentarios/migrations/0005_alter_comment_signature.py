# Generated by Django 4.2.4 on 2023-08-22 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0004_rename_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='signature',
            field=models.CharField(default='Firma', max_length=100),
        ),
    ]