from rest_framework import serializers
from .models import*


class BaseSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(BaseSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            for field_name in remove_fields:
                self.fields.pop(field_name)


#SERIALIZER TO GET USER PROFILE
class UserProfileSerializer(BaseSerializer):
   
    def __init__(self, *args, **kwargs):
        super(UserProfileSerializer, self).__init__(*args, **kwargs)
    username = serializers.ReadOnlyField(source='fetch_username')
    img_url = serializers.ReadOnlyField(source='fetch_image')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")


    class Meta:
        model = Profile
        fields = (
            'username', 'first_name', 'last_name', 'bio', 'img_url',
             'created_at', 'updated_at'
        )
        
#SERIALIZER TO UPDATE USERS PROFILE
class UpdateUserProfileSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Profile
        fields = (
            'first_name', 'last_name', 'bio', 'image'
        )

#SERIALIZER FOR A LIST OF ALL UserS
class UserListSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Profile
        fields = '__all__'