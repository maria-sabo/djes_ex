# Generated by Django 2.0 on 2020-04-11 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True)),
                ('datebirth', models.DateField()),
                ('datedeath', models.DateField()),
                ('countrybirth', models.TextField()),
                ('note', models.CharField(default='', max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Museum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('city', models.TextField()),
                ('country', models.TextField()),
                ('yearfoundation', models.IntegerField()),
                ('note', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('note', models.TextField(default='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictures.Author')),
                ('museum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictures.Museum')),
            ],
        ),
    ]
