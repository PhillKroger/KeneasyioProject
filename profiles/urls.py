from django.urls import path
from profiles.views import login_view, logout_view, register_view, user_account, other_account, verify_user


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', user_account, name='profile'),
    path('user/<int:account_id>/', other_account, name='other_account'),
    path('verify_user/', verify_user, name='verify_user'),
    path('register/', register_view, name='register'),
]
