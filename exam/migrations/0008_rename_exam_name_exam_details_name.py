# Generated by Django 4.0.4 on 2022-05-07 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_exam_details_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam_details',
            old_name='exam_name',
            new_name='name',
        ),
    ]