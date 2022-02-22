from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.



class UserManager(BaseUserManager):
    def create_user(self, email, password=None,is_active=True,is_staff=False, is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        if not password:
            raise ValueError('Users must have an password to login')

        user_obj = self.model(
            email=self.normalize_email(email),
        )

        user_obj.set_password(password)
        user_obj.staff= is_staff
        user_obj.admin=is_admin
        user_obj.active= is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        # user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,primary_key=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
    
    objects = UserManager()

class shipping_address(models.Model):
    #confrim_password = models.CharField(max_length=100)
    #instrument_purchase = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    location = models.TextField(primary_key=True,max_length=500)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.name



class customer_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    joined_date = models.DateTimeField(default=timezone.now()) 
    profile_pic = models.ImageField(upload_to='accounts/profile_pics')
    #profile_pic = models.BinaryField() #models.FileField() #models.AutoField() #models.ImageField()
    #address = models.ForeignKey(shipping_address, on_delete=models.DO_NOTHING, default=False)
    def __str__(self):
        #return f'{self.user.email} Profile'
        return f'{self.name}"s profile'
        
