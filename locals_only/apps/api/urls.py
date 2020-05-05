from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, CategoryActivity, SingleCategoryActivity, ActivityViewSet,
    PublicActivity # PublicActivityDetail
)

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('activities', ActivityViewSet, basename='activities')
# router.register('public-activities', PublicActivityDetail, basename='public-activities')

custom_urlpatterns = [
    url(r'categories/(?P<category_pk>\d+)/activities$', CategoryActivity.as_view(), name='category_activities'),
    url(r'categories/(?P<category_pk>\d+)/activities/(?P<pk>\d+)$', SingleCategoryActivity.as_view(),
        name='single_category_activity'),
    url(r'public-activities/$', PublicActivity.as_view(), name='public_activities'),
    # url(r'public-activities/(?P<pk>\d+)/$', PublicActivityDetail.as_view(), name='public_activity_detail'),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns

