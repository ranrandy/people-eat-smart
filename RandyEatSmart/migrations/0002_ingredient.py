# Generated by Django 3.2.5 on 2021-07-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RandyEatSmart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ingredientid', models.IntegerField(db_column='IngredientID', primary_key=True, serialize=False)),
                ('ingredientname', models.CharField(db_column='IngredientName', max_length=255)),
                ('calorie', models.IntegerField(blank=True, db_column='Calorie', null=True)),
                ('protein', models.FloatField(blank=True, db_column='Protein', null=True)),
                ('fat', models.FloatField(blank=True, db_column='Fat', null=True)),
                ('carbohydrate', models.FloatField(blank=True, db_column='Carbohydrate', null=True)),
            ],
            options={
                'db_table': 'Ingredient',
                'managed': False,
            },
        ),
    ]