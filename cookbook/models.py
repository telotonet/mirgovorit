from django.db import models


class Product(models.Model):
    name = models.CharField("Название продукта", max_length=255)
    times_used = models.PositiveIntegerField("Использовано раз", default=0)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    name     = models.CharField("Название рецепта", max_length=255)
    products = models.ManyToManyField(Product, through='RecipeProduct', verbose_name="Продукт")

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name


class RecipeProduct(models.Model):
    recipe  = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    weight  = models.PositiveSmallIntegerField("Вес продукта")

    class Meta:
        verbose_name = "Продукт в рецепте"
        verbose_name_plural = "Продукты в рецептах"
        unique_together = [['recipe', 'product']]

    def __str__(self):
        return f"{self.product.name} в {self.recipe.name}"
