from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import *

# 7012522984

urlpatterns = [
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),  
    # path('logout/', UserViewSet.as_view({'post': 'logout'}), name='logout'),
    # path('update_profile/', UserViewSet.as_view({'post': 'update_profile'}), name='update_profile'),
    # path('view_profile/', UserViewSet.as_view({'get': 'view_profile'}), name='view_profile'),
    # path('put_update_profile/', UserViewSet.as_view({'put': 'put_update_profile'}), name='put_update_profile'),
    # path('delete_profile/', UserViewSet.as_view({'delete': 'delete_profile'}), name='delete_profile'),
    # path('delete_user_by_mobile/', UserViewSet.as_view({'delete': 'delete_user_by_mobile'}), name='delete_user_by_mobile'),
    # path('change-mobile/', ChangeMobileNumberView.as_view(), name='change_mobile'),

    path('update_profile/<str:uid>/', UpdateProfileView.as_view(), name='update-profile'),
    path('view_profile/<str:uid>/', ViewProfileView.as_view(), name='view-profile'),
    path('delete_profile/<str:uid>/', DeleteProfileView.as_view(), name='delete-profile'),
    path('create_profile/<str:uid>/', CreateProfileView.as_view(), name='create-profile'),

]