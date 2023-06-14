from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import viewsets
from .models import Form, Submit
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
    permission_classes = [permissions.IsAuthenticated]
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
    def get_queryset(self):
        user = self.request.user
        return Form.objects.filter(user=user)
    
    def list(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id') 
        queryset = self.filter_queryset(self.get_queryset())

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class SubmitViewSet(viewsets.ModelViewSet):
    queryset = Submit.objects.all()
    serializer_class = FormSerializer
    @swagger_auto_schema(
        operation_description="List submits to a specific form",
        manual_parameters=[
            openapi.Parameter(
                'form_id',
                openapi.IN_QUERY,
                description="Form ID",
                type=openapi.TYPE_INTEGER
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        form_id = request.GET.get('form_id') 
        queryset = self.filter_queryset(self.get_queryset())

        if form_id:
            queryset = queryset.filter(form_id=form_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
