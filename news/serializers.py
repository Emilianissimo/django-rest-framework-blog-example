from django.utils import timezone
from rest_framework import serializers

from news.models import Category, Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    body = serializers.CharField(required=True, style={'base_template': 'textarea.html'})
    image = serializers.ImageField(required=False, allow_null=True)
    category = serializers.ReadOnlyField(source='category.to_dict')
    created_at = serializers.DateTimeField(required=False, default=timezone.now)

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'title',
            'body',
            'image',
            'category',
            'created_at',
        ]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.image = validated_data.get('image', instance.image)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    posts = PostSerializer(many=True, read_only=True, source='post_set')
    created_at = serializers.DateTimeField(required=False, default=timezone.now)

    class Meta:
        model = Category
        fields = [
            'url',
            'id',
            'title',
            'created_at',
            'posts',
        ]

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


''' MIXIN KIND '''

''' GENERIC KIND '''
