from django.forms import ValidationError
from rest_framework import serializers
from .models import FndUser
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator

# Request and create a new user
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=150,
        min_length=8,
        write_only=True, 
        required=True
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=FndUser.objects.all(),
                message='user with this email already exists'
            )
        ]
    )
   

    class Meta:
        model = FndUser
        fields = ['email', 'username', 'password', 'first_name']

    def create(self, validated_data):
        return FndUser.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['first_name'],
            validated_data['password']
        )


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, allow_blank=True)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True, allow_blank=True)
    token = serializers.CharField(max_length=255, read_only=True)

    #method to validate that what the user logged in is what is in the database
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        #raise error if email and password are not provided
        #we pass in email as username since we declared it in the models
        if not email and not password:
                resp = {
                    'email': 'An email address is required to log in.',
                    'password': 'A password is required to log in.'
                }
                raise serializers.ValidationError(resp)

        # check if user exists
        user = authenticate(username=email, password=password)

        #raise error if authenticate which handles checking for user returns none
        if user is None:
                resp = {
                    'credentials': 'Wrong email or password.'
                }
                raise serializers.ValidationError(resp)

        #raise error if user has been deactivated.use django flag on user model called is_active        
        if not user.is_active:
                raise serializers.ValidationError(
                    'This user has been deactivated.'
                )
        return {
            'email': user.email,
            'username': user.username,
            'token': user.token,
        }


#handle serialization and deserialization of user
class FndUserSerializer(serializers.ModelSerializer):
     password = serializers.CharField(
        max_length=150,
        min_length=8,
        write_only=True, 
        required=True
    )
     class Meta:
        model = FndUser
        fields = ('email', 'username', 'token', 'password')

#update the user
def update(self,instance,validated_data):
    password = validated_data.pop('password', None)# to remove password from validated data then iterate it since they are hashed
    for(key, value)in validated_data.items():
        setattr(instance,key,value)

    if password is not None:
        instance.set_password(password)
    instance.save()
    return instance