from rest_framework import serializers
from .models import BlogPost
 
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('__all__')
    def validate_title(self,value):
        x = BlogPost.objects.all().filter(title = value)
        if x:
            raise serializers.ValidationError("Title should be unique")