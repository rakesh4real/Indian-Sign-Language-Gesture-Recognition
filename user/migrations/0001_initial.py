# Generated by Django 2.2.1 on 2019-06-26 07:09

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
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email1', models.EmailField(max_length=254, null=True)),
                ('Email2', models.EmailField(max_length=254, null=True)),
                ('Email3', models.EmailField(max_length=254, null=True)),
                ('Email4', models.EmailField(max_length=254, null=True)),
                ('Email5', models.EmailField(max_length=254, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]