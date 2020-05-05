# Generated by Django 3.0.6 on 2020-05-05 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20200505_2048'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('details', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='api.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.User')),
            ],
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]
