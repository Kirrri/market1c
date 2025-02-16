from django.contrib import admin
from django.urls import path, include
from . import views
from .views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('profile/', include('profile.urls')),
    path('market/', include('market.urls')),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_view, name='logout'),
]
