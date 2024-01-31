from django.urls import path
from django.views.generic import TemplateView

from .views.login import LoginCreateView, LoginView
from .views.signup import SignupView, UserCreateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signup/user_create/', UserCreateView.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),
    path(
        'login/login_create/', LoginCreateView.as_view(), name='login_create'
    ),
]
