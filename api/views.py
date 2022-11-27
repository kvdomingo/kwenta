from rest_framework.viewsets import ModelViewSet

from .models import Item, ItemGroup, ItemPerson, Person
from .serializers import (
    ItemGroupSerializer,
    ItemPersonSerializer,
    ItemSerializer,
    PersonSerializer,
)


class ItemGroupViewSet(ModelViewSet):
    queryset = ItemGroup.objects.all()
    serializer_class = ItemGroupSerializer


class ItemPersonViewSet(ModelViewSet):
    queryset = ItemPerson.objects.all()
    serializer_class = ItemPersonSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
