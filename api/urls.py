from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('auth/register', views.CreateUser.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),

    path("users/", views.UserList.as_view()),
    path("users/<int:pk>", views.UserDetalis.as_view()),

    path("articles/", views.ArticleList.as_view()),
    path("articles/<int:pk>/", views.ArticleDetail.as_view()),

    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
