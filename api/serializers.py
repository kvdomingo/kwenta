from rest_framework import serializers

from .models import Item, ItemGroup, ItemPerson, Person


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = "__all__"


class ItemPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPerson
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
