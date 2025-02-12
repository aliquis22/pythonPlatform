# Generated by Django 5.0.3 on 2024-05-28 17:01


import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemtest',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='problemtest',
            name='test',
        ),
        migrations.AddField(
            model_name='code',
            name='problem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='problems.problem'),
        ),
        migrations.AddField(
            model_name='code',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='test',
            name='problem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='problems.problem'),
        ),
        migrations.AlterField(
            model_name='code',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.DeleteModel(
            name='ProblemCode',
        ),
        migrations.DeleteModel(
            name='ProblemTest',
        ),
    ]
