# myapp/views.py
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import exception_handler
from django.contrib.auth import get_user_model, authenticate
from django.db import models
from .models import Friends, CustomUser, FriendRequest
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    FriendsSerializer,
    UserSerializer,
    FriendRequestSerializer,
    UserSearchSearializer,
)
from django.utils import timezone
from datetime import timedelta


User = get_user_model()


class HomeView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Welcome to social media app."})


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "user": {"id": user.id, "email": user.email, "name":user.fullname},
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserSearchView(generics.ListAPIView):
    serializer_class = UserSearchSearializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = CustomUser.objects.all()
        name_search = self.request.query_params.get("name", None)
        email_search = self.request.query_params.get("email", None)
        current_user = self.request.user

        queryset = queryset.exclude(id=current_user.id)

        if name_search:
            queryset = queryset.filter(fullname__icontains=name_search)

        if email_search:
            queryset = queryset.filter(email__iexact=email_search)

        return queryset


class SendFriendRequestView(generics.CreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        minute_ago = timezone.now() - timedelta()
        recent_request = FriendRequest.objects.filter(
            sender=request.auth["user_id"], timestamp=minute_ago
        ).count()

        if recent_request >= 3:
            return Response({"detail": "You cannot send more than 3 friend request"})

        request_exists = FriendRequest.objects.filter(
            sender=request.auth["user_id"], receiver=request.data["receiver"]
        ).exists()

        if request_exists:
            return Response({"detail": "Friend request already exist"})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(sender=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AcceptFriendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        try:
            friend_request = FriendRequest.objects.get(
                sender=pk, receiver=request.user, status="pending"
            )
            friend_request.accept()
            return Response(
                {"detail": "Friend request accepted"}, status=status.HTTP_200_OK
            )
        except FriendRequest.DoesNotExist:
            return Response(
                {"detail": "Friend request not found"}, status=status.HTTP_404_NOT_FOUND
            )


class RejectFriendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        try:
            friend_request = FriendRequest.objects.get(
                sender=pk, receiver=request.user, status="pending"
            )
            friend_request.reject()
            return Response(
                {"detail": "Friend request rejected"}, status=status.HTTP_200_OK
            )
        except FriendRequest.DoesNotExist:
            return Response(
                {"detail": "Friend request not found"}, status=status.HTTP_404_NOT_FOUND
            )


class ListFriendsView(generics.ListAPIView):
    serializer_class = FriendsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Friends.objects.filter(models.Q(user=user) | models.Q(friend=user))


class ListPendingFriendRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(
            sender=self.request.user, status="pending"
        )


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return response

    custom_response_data = {
        "error": "An error occurred",
        "detail": str(exc), 
        "status_code": response.status_code,
    }

    if response.status_code == status.HTTP_404_NOT_FOUND:
        custom_response_data["detail"] = "Resource not found"

    # Return the custom response
    return Response(custom_response_data, status=response.status_code)
