from django.urls import path
# from views import index, chat
from . import views
urlpatterns = [
    path('', views.index, name="Home"),
    path('chat/<room_code>', views.chat),
]