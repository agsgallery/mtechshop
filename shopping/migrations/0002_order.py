# Generated by Django 2.2 on 2022-07-07 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
                ('orderdate', models.DateField()),
                ('orderon', models.DateField(auto_now=True)),
                ('productname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.products')),
            ],
        ),
    ]