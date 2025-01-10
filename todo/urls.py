from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewSetExample, DetailMixinsExample, MixinsExample, GenericExample, DetailGenericExample

router = DefaultRouter()
router.register('', ViewSetExample)

urlpatterns = [
    path("TitleViewSet/", include(router.urls)),
    path("TitleMixins/", MixinsExample.as_view(), name='Mixins'),
    path("TitleDetailMixins/<int:pk>",
         DetailMixinsExample.as_view(), name="DetailMixins"),
    path("TitleGenerics/", GenericExample.as_view(), name="GenericApiView"),
    path("DetailGenerics/<int:pk>", DetailGenericExample.as_view(),
         name="DetailGenericsExample")
]
