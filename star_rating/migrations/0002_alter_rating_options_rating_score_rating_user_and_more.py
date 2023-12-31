# Generated by Django 4.2.7 on 2023-11-04 22:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('star_rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={},
        ),
        migrations.AddField(
            model_name='rating',
            name='score',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Terrible'), (2, 'Poor'), (3, 'Average'), (4, 'Very Good'), (5, 'Excellent')], default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user',)},
        ),
        migrations.RemoveField(
            model_name='rating',
            name='five',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='four',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='one',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='three',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='two',
        ),
    ]
