from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('recipe-list', views.RecipeViewSet)
router.register('tag-list', views.TagsViewSet)
router.register('ingredient-list', views.IngredientViewSet)


app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
