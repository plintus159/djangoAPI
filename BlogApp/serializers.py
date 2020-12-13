from rest_framework import serializers
from BlogApp.models import BlogTypes, Blogs

class BlogTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogTypes
        fields =('BlogTypeId',
                'BlogTypeName')

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields =('BlogId',
                'BlogName',
                'Type',
                'DateCreated',
                'PhotoFileName')