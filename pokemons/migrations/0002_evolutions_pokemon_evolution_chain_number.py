# Generated by Django 4.1.5 on 2023-02-20 01:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evolutions',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('first_form', models.CharField(max_length=65)),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='evolution_chain_number',
            field=models.ForeignKey(
                default=None, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='pokemons.evolutions'),
        ),
    ]