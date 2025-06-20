# Generated by Django 5.2.3 on 2025-06-18 07:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='Student Full Name')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='Student Email')),
                ('semester', models.CharField(blank=True, choices=[('SEM_ONE', 'Semester One'), ('SEM_TWO', 'Semester Two'), ('SEM_THREE', 'Semester Three'), ('SEM_FOUR', 'Semester Four'), ('SEM_FIVE', 'Semester Five'), ('SEM_SIX', 'Semester Six'), ('SEM_SEVEN', 'Semester Seven'), ('SEM_EIGHT', 'Semester Eight')], default='N/A', max_length=20, null=True)),
                ('phone_no', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
                'ordering': ['-full_name'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='teacher Full Name')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='teacher Email')),
                ('department', models.CharField(blank=True, choices=[('BCA', 'Bachelor of Computer Application'), ('BEI', 'Bachelor of Electronics and Information'), ('BCE', 'Bachelor of Civil Engineering'), ('BCT', 'Bachelor of Computer Engineering')], default='N/A', max_length=20, null=True)),
                ('phone_no', models.IntegerField()),
                ('join_date', models.DateField(default='Join Date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teachers',
                'ordering': ['-full_name'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Material Title')),
                ('category', models.CharField(choices=[('SLIDE', 'Chapter Slide'), ('A text book', 'TEXT_BOOK'), ('A reference boook', 'REFERENCE_BOOK'), ('OLD_QUESTION', 'Precious board exam question'), ('AUDIO_BOOK', 'An audio book')], default='N/A', max_length=30, verbose_name='select category')),
                ('subject', models.CharField(choices=[('Software Engineering', 'BCTOO1'), ('BCT002', 'System Analysis and Design'), ('BCT003', 'Data Structure'), ('BCT004', 'Data Communication'), ('Mathematics', 'BCT005')], default='N/A', max_length=100, verbose_name='Subject')),
                ('description', models.CharField(blank=True, default='description', max_length=255, null=True, verbose_name='Description of Material')),
                ('uploaded_date', models.DateField(default='Uploaded_Date', verbose_name='Uploaded_Date')),
                ('Material_file', models.FileField(blank=True, default='N/A', null=True, upload_to='material', verbose_name='select file')),
                ('teacher', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='core.teacher', verbose_name='Uploaded By')),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materials',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Assignment Title')),
                ('start_date', models.DateField(default='Start_Date', verbose_name='Start_Date')),
                ('end_date', models.DateField(default='END_Date', verbose_name='End_Date')),
                ('question_file', models.FileField(blank=True, null=True, upload_to='assignments/question/', verbose_name='select_Assignment_file')),
                ('question', models.TextField(blank=True, null=True, verbose_name='Assignment_Question')),
                ('remark', models.CharField(max_length=100, verbose_name='Assignment Details')),
                ('full_mark', models.FloatField()),
                ('subject', models.CharField(choices=[('Software Engineering', 'BCTOO1'), ('BCT002', 'System Analysis and Design'), ('BCT003', 'Data Structure'), ('BCT004', 'Data Communication'), ('Mathematics', 'BCT005')], default='N/A', max_length=100, verbose_name='Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.teacher', verbose_name='Uploaded By')),
            ],
            options={
                'verbose_name': 'assignment',
                'verbose_name_plural': 'assignments',
                'ordering': ['-title'],
            },
        ),
    ]
