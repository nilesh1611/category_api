from rest_framework import serializers
from django.db.models import fields
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('category', 'subcategory', 'name', 'price')









#     child_categories = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Category
#         fields = ['id', 'name', ' child_categories']
#
#         def get_child_categories(self, category):
#             serializer = self.__class__(category.child_categories.all(), many=True)
#             return serializer.data
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id', 'name', ' child_categories']


