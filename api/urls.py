from rest_framework.routers import SimpleRouter

from .views import ItemGroupViewSet, ItemPersonViewSet, ItemViewSet, PersonViewSet

router = SimpleRouter(trailing_slash=False)
router.register("item", ItemViewSet)
router.register("itemGroup", ItemGroupViewSet)
router.register("itemPerson", ItemPersonViewSet)
router.register("person", PersonViewSet)

urlpatterns = [
    *router.urls,
]
