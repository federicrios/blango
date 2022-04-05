from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from blog.api.views import PostList, PostDetail
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("token-auth/", views.obtain_auth_token),
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("jwt/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
