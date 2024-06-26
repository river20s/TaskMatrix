# Generated by Django 5.0.6 on 2024-05-28 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='목록 이름')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.IntegerField(choices=[(1, '중요하고 긴급함'), (2, '중요하지만 긴급하지 않음'), (3, '긴급하지만 중요하지 않음'), (4, '중요하지도 긴급하지 않음')], default=4, verbose_name='카테고리'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='설명'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.tasklist', verbose_name='할일 목록'),
            preserve_default=False,
        ),
    ]
