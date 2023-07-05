from rest_framework import serializers
from .models import Snippet, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class SnippetSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Snippet
        fields = '__all__'
        
    def create(self, validated_data):
        tag_title = validated_data.pop('tag')
        # Check if the tag with the same title exists
        tag, _ = Tag.objects.get_or_create(title=tag_title)
        snippet = Snippet.objects.create(tag=tag, **validated_data)
        return snippet