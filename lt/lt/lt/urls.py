"""lt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rpc4django.views import serve_rpc_request

from license_server import views as home_view

admin.site.site_title = 'License Server'
admin.site.site_header = 'License Server'

urlpatterns = (
    # rpc4django will need to be in your Python path
    url(r'^rpc$', serve_rpc_request),
    url(r'^license/', include('license_server.urls')),
    url(r'^$', home_view.home_page, name='home_page'),
    url(r'^admin/', admin.site.urls),
)