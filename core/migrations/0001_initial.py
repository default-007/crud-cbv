# Generated by Django 4.0.3 on 2022-03-05 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Core',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('excerpt', models.TextField(max_length=500)),
                ('slug', models.SlugField(max_length=100)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='core', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
