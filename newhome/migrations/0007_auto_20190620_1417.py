# Generated by Django 2.2.2 on 2019-06-20 08:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('newhome', '0006_auto_20190620_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_sem',
            field=models.CharField(help_text='Student Sem', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.UUIDField(default=uuid.uuid4, help_text='generated unique id for student', primary_key=True, serialize=False, verbose_name='student Id'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(help_text='Student Name', max_length=100, null=True),
        ),
    ]
