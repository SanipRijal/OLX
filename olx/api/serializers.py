from rest_framework import serializers
from olxapp.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'price', 'model', 'category', 'color', 'size', 'manufacture_date', 'description',)
        model = Product

    category = serializers.SerializerMethodField('get_category_name')

    def get_category_name(self, obj):
        return obj.category.name

