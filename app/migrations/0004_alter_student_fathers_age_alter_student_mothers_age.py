# Generated by Django 4.2.1 on 2023-10-20 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fathers_age',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mothers_age',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]