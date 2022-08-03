# Generated by Django 4.0.6 on 2022-08-02 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя учителя')),
            ],
        ),
        migrations.RemoveField(
            model_name='pair',
            name='subject',
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='Номер группы'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pair',
            name='day',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.day'),
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.subject', verbose_name='Предмет')),
                ('teacher', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.teacher', verbose_name='Имя учителя')),
            ],
        ),
        migrations.AddField(
            model_name='pair',
            name='lessons',
            field=models.ManyToManyField(to='app.lessons'),
        ),
    ]
