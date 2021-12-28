from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import views, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt import authentication
from .serializers import UserSerializer, GroupSerializer


class SampleAPI1(views.APIView):
    # Specify JWT authentication is the only authentication method allowed
    # and the APIView is only accessible if a user sends a request with an
    # access token.
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        return Response([{'a': 'SampleAPI1'}])

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    # Specify JWT authentication is the only authentication method allowed
    # and the APIViewSet is only accessible if a user sends a request with
    # an access token.
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]