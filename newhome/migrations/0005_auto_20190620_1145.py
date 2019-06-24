# Generated by Django 2.2.2 on 2019-06-20 06:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('newhome', '0004_auto_20190620_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.UUIDField(default=uuid.uuid4, help_text='generated unique id for customer', primary_key=True, serialize=False, verbose_name='customer Id')),
                ('student_name', models.CharField(help_text='Customer Name', max_length=100, null=True)),
                ('borrow_date', models.DateField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('total_book_borrowed', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], max_length=1, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('book_name', models.ForeignKey(help_text='Book Name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='newhome.Book')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
