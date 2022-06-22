from core.models import Recipe
from rest_framework.serializers import ModelSerializer


class RecipeSr(ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSr):
    """Serializer for recipe detail view."""

    class Meta(RecipeSr.Meta):
        fields = RecipeSr.Meta.fields + ['description']
