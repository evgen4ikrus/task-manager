# Generated by Django 4.2.5 on 2023-10-02 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название'),
        ),
    ]
