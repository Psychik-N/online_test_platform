# Generated by Django 4.0.4 on 2022-05-07 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
        ('exam', '0004_alter_exam_details_created_by_alter_exam_details_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_details',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recruiter.recruiter_profile_model'),
        ),
    ]