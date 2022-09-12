from django.forms import SlugField
from rest_framework import serializers
from .models import Singer,Song

class SingerSerializers(serializers.ModelSerializer):
    # Song=serializers.StringRelatedField(many=True,read_only=True)
    # Song=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # Song=serializers.HyperlinkedIdentityField(many=True,read_only=True ,view_name='Song')
    # Song=serializers.SlugRelatedField(many=True,read_only=True ,slug_field='title')
    # Song=serializers.SlugRelatedField(many=True,read_only=True ,slug_field='duration')
    Song=serializers.HyperlinkedIdentityField(many=True,read_only=True ,view_name='song-detail')

    class Meta:
        model= Singer
        fields=['id','name','gender','Song']


class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields="__all__"