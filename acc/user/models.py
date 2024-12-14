from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone_number, email, username, user_type, password=None):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('Username is required')
        if not user_type:
            raise ValueError('User type is required')

        email = self.normalize_email(email)

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            username=username,
            user_type=user_type,
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, phone_number, email, username, user_type, password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            username=username,
            user_type=user_type,
            password=password,
        )
        user.is_active = True
        user.is_admin = True
        user.is_superadmin = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser):
    USER_TYPE_CHOICES = (
        ('HOD', 'Head of Department'),
        ('Staff', 'Staff'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'email', 'user_type']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return self.is_admin


class UserCriteriaLink(models.Model):
    CRITERIA_LIST = (
        # criteria 1
        ('1_1_1', "Criteria 1.1.1"),
        ('1_2_2', "Criteria 1.2.2"),
        ('1_3_1', "Criteria 1.3.1"),
        ('1_3_2', "Criteria 1.3.2"),

        # criteria 2
        ('2_3_1', "Criteria 2.3.1"),
        ('2_4_2', "Criteria 2.4.2"),
        ('2_5_1', "Criteria 2.5.1"),
        ('2_6_1', "Criteria 2.6.1"),
        ('2_6_2', "Criteria 2.6.2"),
        ('2_6_3', "Criteria 2.6.3"),
        ('2_7_1', "Criteria 2.7.1"),

        # criteria 3
        ('3_1_1', "Criteria 3.1.1"),
        ('3_2_1', "Criteria 3.2.1"),
        ('3_2_2', "Criteria 3.2.2"),
        ('3_3_1', "Criteria 3.3.1"),
        ('3_3_2', "Criteria 3.3.2"),
        ('3_4_1', "Criteria 3.4.1"),
        ('3_4_2', "Criteria 3.4.2"),
        ('3_4_3', "Criteria 3.4.3"),
        ('3_5_1', "Criteria 3.5.1"),

        # criteria 4
        ('4_1_1', "Criteria 4.1.1"),
        ('4_1_2', "Criteria 4.1.2"),
        ('4_2_1', "Criteria 4.2.1"),
        ('4_3_1', "Criteria 4.3.1"),
        ('4_4_1', "Criteria 4.4.1"),

        # criteria 5
        ('5_1_1', "Criteria 5.1.1"),
        ('5_1_2', "Criteria 5.1.2"),
        ('5_1_3', "Criteria 5.1.3"),
        ('5_1_4', "Criteria 5.1.4"),
        ('5_2_1', "Criteria 5.2.1"),
        ('5_2_2', "Criteria 5.2.2"),
        ('5_3_1', "Criteria 5.3.1"),
        ('5_3_2', "Criteria 5.3.2"),
        ('5_4_1', "Criteria 5.4.1"),

        # criteria 6
        ('6_1_1', "Criteria 6.1.1"),
        ('6_2_1', "Criteria 6.2.1"),
        ('6_2_2', "Criteria 6.2.2"),
        ('6_3_1', "Criteria 6.3.1"),
        ('6_3_2', "Criteria 6.3.2"),
        ('6_3_3', "Criteria 6.3.3"),
        ('6_4_1', "Criteria 6.4.1"),
        ('6_5_1', "Criteria 6.5.1"),
        ('6_5_2', "Criteria 6.5.2"),

        # criteria 7
        ('7_1_1', "Criteria 7.1.1"),
        ('7_1_2', "Criteria 7.1.2"),
        ('7_1_3', "Criteria 7.1.3"),
        ('7_1_4', "Criteria 7.1.4"),
        ('7_2_1', "Criteria 7.2.1"),
        ('7_3_1', "Criteria 7.3.1"),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    criteria = models.CharField(max_length=10, choices=CRITERIA_LIST)


