from django.urls import path
from django.views.generic import TemplateView

from .views import LoginCreateView, LoginView, SignupView, UserCreateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path(
        'plans/',
        TemplateView.as_view(template_name='plans.html'),
        name='plans',
    ),
    path(
        'blog/', TemplateView.as_view(template_name='blog.html'), name='blog'
    ),
    path(
        'support/',
        TemplateView.as_view(template_name='support.html'),
        name='support',
    ),
    path(
        'about/',
        TemplateView.as_view(template_name='about.html'),
        name='about',
    ),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signup/user_create/', UserCreateView.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),
    path(
        'login/login_create/', LoginCreateView.as_view(), name='login_create'
    ),
    path(
        'app/', TemplateView.as_view(template_name='base/app.html'), name='app'
    ),
]
