from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from .models import User, listings, bids, comments
from .forms import *


def index(request):
    listing = bids.objects.all().select_related('auction')
    return render(request, "auctions/index.html",{
        "Listings": listing
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def newbid(request):
    listing = bids.objects.all().select_related('auction').filter(auction_id=request.POST["listng"])
    minimum = listing[0].bidprice + Decimal(.01).quantize(Decimal('0.01'))
    return render(request,"auctions/bid.html",{
        "Listings": listing,
        "minimum": minimum
    })
    
    

@login_required
def newitem(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        category = request.POST["category"]
        imgUrl = request.POST["imgUrl"]
        price = request.POST["price"]
        user = request.user
        
        try:
            listing = listings(title= title,description= description,active=True,owner=request.user,category=category,image=imgUrl)
            listing.save()
            bid = bids(auction=listing,bidder=user,bidprice=price)
            bid.save()
        except:
            return render(request, "auctions/index.html",{
                "message": "Something went wrong try again."
            })

        return HttpResponseRedirect(reverse("index"))
    else:
        form = NewItemForm
        return render(request, "auctions/newlisting.html", {'form': form})