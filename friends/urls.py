# myapp/urls.py
from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    UserListView,
    SendFriendRequestView,
    AcceptFriendRequestView,
    RejectFriendRequestView,
    ListPendingFriendRequestsView,
    ListFriendsView,
    UserSearchView
)

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("search", UserSearchView.as_view(), name="user-search"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("friends/send/", SendFriendRequestView.as_view(), name="send_friend_request"),
    path(
        "friends/accept/<int:pk>/",
        AcceptFriendRequestView.as_view(),
        name="accept_friend_request",
    ),
    path(
        "friends/reject/<int:pk>/",
        RejectFriendRequestView.as_view(),
        name="reject_friend_request",
    ),
    path("friends/", ListFriendsView.as_view(), name="list_friends"),
    path(
        "friends/pending/",
        ListPendingFriendRequestsView.as_view(),
        name="list_pending_friend_requests",
    ),
]
