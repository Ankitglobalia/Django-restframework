

from rest_framework import serializers
from.models import Student



# Model Serializer class
class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city']


# # Regular serializers
# class Studentserializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name=serializers.CharField(max_length=100)
#     roll=serializers.IntegerField()
#     city=serializers.CharField(max_length=100)


#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         print(instance.name)
#         instance.name= validated_data.get('name',instance.name)  
#         print(instance.name)
#         instance.roll= validated_data.get('roll',instance.roll)  
#         instance.city= validated_data.get('city',instance.city)  
#         instance.save()
#         return instance