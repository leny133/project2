from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class listings(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.CharField(max_length=24)
    image = models.URLField(null=True)

class bids(models.Model):
    auction = models.ForeignKey(listings, on_delete= models.PROTECT)
    bidder = models.ForeignKey(User, on_delete= models.PROTECT, related_name= "bidder")
    bidprice = models.DecimalField(decimal_places=2, max_digits=8 )
    winner = models.ForeignKey(User, null=True, related_name="winner", blank = True, on_delete= models.PROTECT)

class comments(models.Model):
    commentUser = models.ForeignKey(User, on_delete= models.PROTECT)
    listingComment = models.ForeignKey(listings, on_delete= models.PROTECT)
    comment = models.CharField(max_length=250)
