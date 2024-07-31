from rest_framework import serializers
from ..models import Author

# class Author(models.Model):
#     name = models.CharField(max_length=200)


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance



# def books(request):
#     getAllBooks= Book.objects.all()
#     return render(request,'bookApp/index.html',{'getAllBooks':getAllBooks})

