from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Category, Activity
from .serializers import CategorySerializer, ActivitySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # list categories for current logged in user
        queryset = Category.objects.all().filter(owner=self.request.user)
        return queryset

    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        category = Category.objects.filter(
            name=request.data['name'],
            owner=request.user
        )
        if category:
            msg = 'Category with this name already exists'
            raise ValidationError(msg)
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        category = Category.objects.get(pk=self.kwargs["pk"])
        if not request.user == category.owner:
            raise PermissionDenied("Only the owner may delete this category")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryActivity(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.kwargs.get('category_pk'):
            category = Category.objects.get(pk=self.kwargs["category_pk"])
            queryset = Activity.objects.filter(
                owner=self.request.user,
                category=category
            )
        return queryset

    serializer_class = ActivitySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SingleCategoryActivity(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.kwargs.get("category_pk") and self.kwargs.get("pk"):
            category = Category.objects.get(pk=self.kwargs["category_pk"])
            queryset = Activity.obects.filter(
                pk=self.kwargs["pk"],
                owner=self.request.user,
                category=category
            )
        return queryset

    serializer_class = ActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Activity.objects.all().filter(owner=self.request.user)
        return queryset

    serializer_class = ActivitySerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied("Only logged in users with accounts can create recipes")
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        recipe = Activity.objects.get(pk=self.kwargs["pk"])
        if not request.user == recipe.owner:
            raise PermissionDenied("Only the owner may delete this recipe")
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        recipe = Activity.objects.get(pk=self.kwargs["pk"])
        if not request.user == recipe.owner:
            raise PermissionDenied("Only the owner may edit this recipe")
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicActivity(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Activity.objects.all().filter(is_puplic=True)
        return queryset

    serializer_class = ActivitySerializer


# class PublicActivityDetail(viewsets.ReadOnlyModelViewSet):
#     permission_classes = (AllowAny,)
#
#     def get_queryset(self):
#         queryset = Activity.objects.all().filter(is_public=True)
#         return queryset
#
#     serializer_class = ActivitySerializer
