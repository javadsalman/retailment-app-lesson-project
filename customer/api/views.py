from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.utils import timezone
from .serializers import RegisterSerializer, CustomerSerializer, CustomerAuthSerializer, SubscriptionSerializer
from ..models import Customer, Subscription, Payment

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    
    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    # permission_classes = [IsAuthenticated,]
    
    def create(self, request, *args, **kwargs):
        auth_serializer = RegisterSerializer(data=request.data)
        if auth_serializer.is_valid():
            auth_serializer.save()
            return Response(auth_serializer.data, status=status.HTTP_201_CREATED)
        return Response(auth_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'])
    def login(self, request):
        user_info = request.data.get('user_info')
        password = request.data.get('password')
        if '@' in user_info:
            user = User.objects.filter(email=user_info).first()
        else:
            user = User.objects.filter(username=user_info).first()
        
        if user and user.check_password(password):
            serializer = CustomerAuthSerializer(instance=user.customer) # type: ignore
            
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(data={'message': 'User info or password is incorrect!'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'])
    def subscribe(self, request):
        customer = request.user.customer
        subscription = Subscription.objects.get(id=request.data.get('subscription_id'))
        customer.subscription = subscription
        customer.subscription_date = timezone.now()
        customer.save()
        payment = Payment.objects.create(
            customer=customer, 
            subscription=subscription, 
            amount=subscription.price,
        )
        payment.save()
        customer_serializer = CustomerSerializer(instance=customer)
        return Response(data=customer_serializer.data, status=status.HTTP_200_OK)

# # Create your views here.
# @api_view(['POST'])
# # @throttle_classes([AnonRateThrottle, UserRateThrottle])
# def register_view(request):
#     print('register', request.data)
#     serializer = RegisterSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# @api_view(['POST'])
# # @throttle_classes([AnonRateThrottle, UserRateThrottle])
# def login_view(request):
#     user_info = request.data.get('user_info')
#     password = request.data.get('password')
#     if '@' in user_info:
#         user = User.objects.filter(email=user_info).first()
#     else:
#         user = User.objects.filter(username=user_info).first()
    
#     if user and user.check_password(password):
#         serializer = CustomerAuthSerializer(instance=user.customer) # type: ignore
        
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     return Response(data={'message': 'User info or password is incorrect!'}, status=status.HTTP_400_BAD_REQUEST)