<<<<<<< HEAD
# Generated by Django 4.1.3 on 2022-11-17 17:00
=======
# Generated by Django 4.1.3 on 2022-11-17 15:12
>>>>>>> 0bf1adc (finished comment functionality)

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(verbose_name='Event Date')),
                ('location', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('B', 'Business Meeting'), ('U', 'UXDI'), ('S', 'Software Engineer'), ('D', 'Designer'), ('F', 'Finance'), ('R', 'Real Estate'), ('I', 'Self-Improvement'), ('M', 'Marketing')], default='B', max_length=1)),
<<<<<<< HEAD
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
=======
>>>>>>> 0bf1adc (finished comment functionality)
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.event')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('comment', models.CharField(max_length=50)),
=======
                ('text', models.CharField(max_length=50)),
>>>>>>> 0bf1adc (finished comment functionality)
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.event')),
            ],
        ),
    ]
