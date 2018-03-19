from django.db import models

from django.conf import settings
from django.conf import settings
# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    CATEGORY_CHOICES = (
        ('Tech', 'Tech'),
        ('Sports', 'Sports'),
        ('Fashion', 'Fashion'),
        ('Food', 'Food'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to=upload_location,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    category = models.CharField(max_length=128,choices=CATEGORY_CHOICES)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "%s/" %(self.id)


class UsersCategories(models.Model):
    user = models.CharField(max_length=128)

    category = models.CharField(max_length=128)

    class Meta:
        unique_together = ["user", "category"]

    def __unicode__(self):
        return self.user

    def __str__(self):
        return self.user
