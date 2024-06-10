from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils import timezone


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email field is must")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(email, password,  **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # objects = CustomUserManager()

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        verbose_name=("groups"),
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",
        blank=True,
        help_text=("Specific permissions for this user."),
        verbose_name=("user permissions"),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Friends(models.Model):
    user = models.ForeignKey(CustomUser, related_name='friend_creater', on_delete=models.CASCADE)
    friend = models.ForeignKey(CustomUser, related_name='friend_setr', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'friend')

    def __str__(self):
        return f"{self.user.email} is friends with {self.friend.email}"


class FriendRequest(models.Model):
    sender = models.ForeignKey(
        CustomUser, related_name="sent_requests", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        CustomUser, related_name="received_requests", on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=(
            ("pending", "Pending"),
            ("accepted", "Accepted"),
            ("rejected", "Rejected"),
        ),
        default="pending",
    )

    class Meta:
        unique_together = ("sender", "receiver")

    def accept(self):
        self.status = "accepted"
        self.save()
        Friends.objects.create(user=self.sender, friend=self.receiver)

    def reject(self):
        self.status = "rejected"
        self.save()
