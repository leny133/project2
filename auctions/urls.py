from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newlisting", views.newitem, name="newitem"),
    path("bid/<int:AuId>", views.newbid, name="newbid"),
    path("categories", views.categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("closedlist", views.closed, name="closedlist"),
    path("categories/<str:selcat>", views.selected, name="selected"),
    path("categories/bid/<int:AuId>", views.newbid, name="newbid"),
    
]
