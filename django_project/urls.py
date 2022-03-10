"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from dajango.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path, include
from accounts import views as user_views
from products.views import *

#from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('OMart.urls')),

    path('add_products/', products_insert_view, name='product-insert'),
    path('products/<product_id>', product_page, name='Omart-view_product_detail'),
    path('products/<product_id>',postJsonData.as_view(), name='post-jason-bid-view'),
    path('my-items/',my_posted_items, name='my_items'),

    path('register/', user_views.register, name='Omart-register'),
    path('login/', user_views.login_view, name='Omart-login'),
    path('logout/', user_views.logout_view, name='Omart-logout'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password-reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password-reset-done'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
