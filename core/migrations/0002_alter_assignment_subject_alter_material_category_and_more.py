# Generated by Django 5.2.3 on 2025-06-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='subject',
            field=models.CharField(choices=[('BCTOO1', 'Software Engineering'), ('BCT002', 'System Analysis and Design'), ('Data Structure', 'BCT003'), ('BCT004', 'Data Communication'), ('Mathematics', 'BCT005')], default='N/A', max_length=100, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='material',
            name='category',
            field=models.CharField(choices=[('SLIDE', 'Chapter Slide'), ('TEXT_BOOK', 'A text book'), ('A reference boook', 'REFERENCE_BOOK'), ('Precious board exam question', 'OLD_QUESTION'), ('An audio book', 'AUDIO_BOOK')], default='N/A', max_length=30, verbose_name='select category'),
        ),
        migrations.AlterField(
            model_name='material',
            name='subject',
            field=models.CharField(choices=[('BCTOO1', 'Software Engineering'), ('BCT002', 'System Analysis and Design'), ('Data Structure', 'BCT003'), ('BCT004', 'Data Communication'), ('Mathematics', 'BCT005')], default='N/A', max_length=100, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.CharField(blank=True, choices=[('BCE', 'Bachelor of Civil Engineering'), ('BEI', 'Bachelor of Electronics and Information'), ('BCT', 'Bachelor of Computer Engineering'), ('BCA', 'Bachelor of Computer Application')], default='N/A', max_length=20, null=True),
        ),
    ]
