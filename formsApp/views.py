from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import routers, serializers, viewsets
from rest_framework.viewsets import ViewSet
from .models import Form
from .serializers import UserSerializer, FormSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = ()
    serializer_class = RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    @swagger_auto_schema(
        operation_description="List forms of a specific user",
        manual_parameters=[
            openapi.Parameter(
                'user_id',
                openapi.IN_QUERY,
                description="User ID",
                type=openapi.TYPE_INTEGER
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id') 
        queryset = self.filter_queryset(self.get_queryset())

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

