# Generated by Django 3.2.16 on 2023-01-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_rename_teacher_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(default='на каникулах', related_name='students', to='school.Teacher'),
        ),
    ]