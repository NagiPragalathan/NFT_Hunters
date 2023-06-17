from django.urls import path
from . import views

from django.conf.urls.static import static
from NFT_Game import settings


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

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
