# Generated by Django 3.2.9 on 2021-11-06 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('artist', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('orignal_release', models.DateField()),
                ('condition', models.CharField(choices=[('M', 'Mint'), ('NM', 'Near Mint'), ('VG+', 'Very Good Plus'), ('VG', 'Very Good'), ('G+', 'Good Plus'), ('G', 'Good'), ('F', 'Fair'), ('P', 'Poor')], default='M', max_length=3)),
            ],
        ),
    ]