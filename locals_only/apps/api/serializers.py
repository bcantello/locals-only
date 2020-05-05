from rest_framework import serializers
from .models import Category, Activity


class ActivitySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Activity
        fields = (
            'id',
            'name',
            'location',
            'description',
            'details',
            'owner',
            'category',
            'created_at',
            'updated_at',
            'is_public',
        )


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    recipes = ActivitySerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'owner',
            'description',
            'activity',
            'created_at',
            'updated_at',
        )
