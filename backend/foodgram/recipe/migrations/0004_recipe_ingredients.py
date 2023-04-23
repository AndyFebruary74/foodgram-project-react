# Generated by Django 3.2 on 2023-04-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20230414_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', through='recipe.IngredientRecipe', to='recipe.Ingredient', verbose_name='Ингредиенты'),
        ),
    ]