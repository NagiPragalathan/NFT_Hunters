from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('browse',views.browse),
    path('profile',views.profile),
    path('details',views.details),
    path('streams',views.streams),
    path('lobby', views.lobby),
    path('room/', views.room),
    path('get_token/', views.getToken),
    path('open_Nft_craft',views.open_Nft_craft),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
]