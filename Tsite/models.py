from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

# Create your models here.

class StudentManager(BaseUserManager):

    def create_user(self, email, username, usn, year, branch, phone_no, password=None):

        if not email:
            raise ValueError("User must have email address")

        if not usn:
            raise ValueError("User must have USN")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            usn = usn,
            year=year,
            branch=branch,
            phone_no=phone_no
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, usn, year, branch, phone_no, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            usn = usn,
            password=password,
            year=year,
            branch=branch,
            phone_no=phone_no
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Student(AbstractBaseUser):

    p = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    usn = models.CharField(max_length=30, unique=True)
    year = models.IntegerField()
    branch = models.CharField(max_length=10)
    phone_regex =  RegexValidator(regex=r'^\+?1?\d{10}$')
    phone_no = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["usn", "username", "year", "branch", "phone_no"]

    object = StudentManager()
    def __str__(self):
         return self.username

    def has_perm(self, perm, object=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True


class Submissions(models.Model):
    a = models.AutoField(primary_key=True)
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    l1 = models.CharField(max_length=200, null=True, blank=True)
    l2 = models.CharField(max_length=200, null=True, blank=True)
    l3 = models.CharField(max_length=200, null=True, blank=True)
    l4 = models.ImageField(null=True, blank=True)
    l5 = models.CharField(max_length=200, null=True, blank=True)
    l1_time = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    l2_time = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    l3_time = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    l4_time = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    l5_time = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name.username
    

    # def save(self, *args, **kws):
    #     try:
    #         um = Answer.objects.get(a=self.a)
    #         update_submission = True
    #     except Answer.DoesNotExist:
    #         update_submission = False

    #     for flag_no in range(1, 6):
    #         flag = f"l{flag_no}"
    #         flag_ts = f"{flag}_time"

    #         now = getattr(self, flag)
    #         if update_submission:
    #             prv = getattr(um, flag)
    #         else:
    #             prv = None

    #         if now != prv:
    #             setattr(self, flag_ts, timezone.now())

    #     super().save(*args, **kws)

    # def __str__(self):
    #     ts = (f"l{x}_time"for x in range(1,6))
    #     submissions = '\n'.join(f"{f} = {getattr(self, f)}" for f in ts)
    #     return f"***\n{self.name!r}\n{submissions}\n***\n"

class AnswersKey(models.Model):

    a = models.AutoField(primary_key=True)
    lvl_1 = models.CharField(max_length=200, null=True, blank=True)
    lvl_2= models.CharField(max_length=200, null=True, blank=True)
    lvl_3 = models.CharField(max_length=200, null=True, blank=True)
    lvl_4= models.ImageField(blank=True, null=True)
    lvl_5 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "ANSWER KEY"
    