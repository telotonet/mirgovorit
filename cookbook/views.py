from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from .models import Recipe, Product, RecipeProduct


@require_GET
def show_recipes_without_product (request):
    product_id = request.GET.get('product_id')

    recipes = Recipe.objects.exclude(products__id=product_id, recipeproduct__weight__gte=10)
    return render(request, 'show_recipes_without_product.html', {'recipes': recipes})


@require_POST
def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    try:
        recipe = Recipe.objects.get(id=recipe_id)
        product = Product.objects.get(id=product_id)
        RecipeProduct.objects.update_or_create(recipe=recipe, product=product, defaults={'weight': weight})
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


@require_POST
def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')

    try:
        recipe_products = RecipeProduct.objects.filter(recipe_id=recipe_id)
        for rp in recipe_products:
            rp.product.times_used += 1
            rp.product.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
