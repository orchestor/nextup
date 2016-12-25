"""nextup URL Configuration

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
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from nextup.views import home, successSignup, expansion, northWest, southWest, northCentral, southCentral, northEast, southEast
from authentication.views import login, signup, checkUserhandle
from music.views import likeSong

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^login', login),
    url(r'^signup', signup),
    url(r'^checkUserhandle', checkUserhandle),
    url(r'^success-signup$', successSignup),
    url(r'^likeSong$', likeSong),
    url(r'^expansion$', expansion),
    url(r'^north-west$', northWest),
    url(r'^south-west$', southWest),
    url(r'^north-central$', northCentral),
    url(r'^south-central$', southCentral),
    url(r'^north-east$', northEast),
    url(r'^south-east$', southEast),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
