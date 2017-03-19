from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)


class User(AbstractUser, BaseModel):
    user_name = models.CharField(max_length=60, unique=True)
    first_name = models.CharField(max_length=90, blank=True, null=True)
    last_name = models.CharField(max_length=90, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=90, blank=True, null=True)
    password_hash = models.CharField(max_length=90)
    country = models.CharField(max_length=90)
    national_id = models.CharField(max_length=90)
    photo = models.CharField(max_length=90, blank=True, null=True)
    role = models.BooleanField(default=False)
    user_type = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Bus(BaseModel):
    bus_model = models.CharField(max_length=90)
    passenger_seats = models.IntegerField(max_length=90)
    name = models.CharField(max_length=90)

    def __str__(self):
        return  self.name


class Route(BaseModel):
    d_from = models.CharField(max_length=90)
    d_to = models.CharField(max_length=90)
    bus_id = models.ForeignKey(Bus, related_name='routes', on_delete=models.CASCADE)

    def __str__(self):
        return  "{} to {}".format(self.d_from, self.d_to)


class Booking(BaseModel):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bookings', on_delete=models.CASCADE)
    destination_id = models.ForeignKey(Route, related_name='destinations', on_delete=models.CASCADE)



# class Post(BaseModel):
#     STATUS_CHOICES = [
#         ('draft', 'Draft'),
#         ('published', 'Published'),
#     ]
#     title = models.CharField(max_length=100, null=False)
#     post = models.TextField()
#     slug = models.SlugField(unique=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
#     date_published = models.DateTimeField(default=timezone.now)
#     tags = TaggableManager() # taggit manager

#     class Meta:
#         ordering = ('-date_published',)

#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super(Post, self).save(*args, **kwargs)


# class Comment(BaseModel):
#     comment = models.TextField()
#     post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.comment
