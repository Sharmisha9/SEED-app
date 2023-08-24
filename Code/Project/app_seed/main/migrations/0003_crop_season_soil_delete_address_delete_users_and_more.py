# Generated by Django 4.1.1 on 2022-10-23 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_users_first_name_alter_users_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Soil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soil_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='crop',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.season'),
        ),
        migrations.AddField(
            model_name='crop',
            name='soil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.soil'),
        ),
    ]
