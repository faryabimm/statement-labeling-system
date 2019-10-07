# Generated by Django 2.2.6 on 2019-10-07 20:13

import crowd_labeling.models
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
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_time', models.FloatField()),
                ('label', models.CharField(choices=[(crowd_labeling.models.LabelChoices(('Positive', '+')), 'Positive'), (crowd_labeling.models.LabelChoices(('Negative', '-')), 'Negative'), (crowd_labeling.models.LabelChoices(('Neutral', '?')), 'Neutral')], max_length=8)),
                ('statement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowd_labeling.Statement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
