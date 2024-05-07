from rest_framework import serializers
from .models import Cat

from rest_framework import serializers
from .models import Cat
from transliterate import translit
import re


class CatSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Cat
        fields = "__all__"
        read_only_fields = ('slug',)

    def create(self, validated_data):
        title = validated_data.get('title')

        # Транслитерация русских слов на кириллице в латиницу
        slug = translit(title, 'ru', reversed=True)
        slug = slug.lower()
        # Замена пробелов на дефисы
        slug = slug.replace(' ', '-')
        slug = re.sub(r'[^a-zA-Z-]', '', slug)

        validated_data['slug'] = slug
        return super().create(validated_data)
