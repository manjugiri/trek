# Generated by Django 3.2.3 on 2021-09-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treck', '0004_safari'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treknep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
