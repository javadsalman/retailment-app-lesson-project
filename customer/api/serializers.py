from rest_framework import serializers
from rest_framework.authtoken.models import Token
from customer.models import Customer
from django.contrib.auth.models import User
from ..models import GENDER_CHOICES, Customer, Subscription


class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password', write_only=True)
    birth_date = serializers.DateField(input_formats=['%Y-%m-%d'])
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    profile_photo = serializers.ImageField()
    company_name = serializers.CharField()
    company_logo = serializers.ImageField()
    address = serializers.CharField()
    token = serializers.SerializerMethodField(read_only=True)
    
    def create(self, validated_data):
        user_info: dict[str, str] = validated_data.pop('user')
        user = User.objects.create_user(**user_info)
        customer = Customer.objects.create(user = user, **validated_data)
        return customer
    
    def get_token(self, customer: Customer):
        token, created = Token.objects.get_or_create(user=customer.user)
        return token.key
    
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        
class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    birth_date = serializers.DateField(input_formats=['%Y.%m.%d'])
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    subscription = SubscriptionSerializer()
    class Meta:
        model = Customer
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'birth_date', 
            'gender', 
            'subscription',
            'subscribtion_date',
            'address',
            'profile_photo',
            'company_name',
            'company_logo',
        ]
        read_only_fileds = ['id', 'subscription',]
        
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
        

class CustomerAuthSerializer(CustomerSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta(CustomerSerializer.Meta):
        fields = CustomerSerializer.Meta.fields + ['token']

    def get_token(self, customer):
        token, created = Token.objects.get_or_create(user=customer.user)
        return token.key
    
