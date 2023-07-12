# Generated by Django 4.2.3 on 2023-07-10 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='tickets',
            name='status',
            field=models.CharField(default='PENDING', max_length=20),
        ),
        migrations.AlterField(
            model_name='flight',
            name='seats_count',
            field=models.IntegerField(default=60),
        ),
        migrations.CreateModel(
            name='CancelledTickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_no', models.CharField(max_length=8, unique=True)),
                ('passenger', models.CharField(max_length=50)),
                ('cancelled_date_time', models.DateTimeField(auto_now_add=True)),
                ('seat_number', models.IntegerField()),
                ('status', models.CharField(default='CANCELLED', max_length=20)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.flight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='arrival', to='mainapp.airports'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departure', to='mainapp.airports'),
        ),
    ]