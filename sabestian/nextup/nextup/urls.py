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
from nextup.views import home, successSignup, expansion, northWest, southWest, northCentral, southCentral, northEast, southEast, alabama, alaska, arizona, arkansas, california, colorado, connecticut, delaware, districtofColumbia, florida, georgia, hawaii, idaho, illinois, indiana, iowa, kansas, kentucky, louisiana, maine, maryland, massachusetts, michigan, minnesota, mississippi, missouri, montana, nebraska, nevada, newHampshire, newJersey, newMexico, newYork, northCarolina, northDakota, ohio, oklahoma, oregon, pennsylvania, rhodeIsland, southCarolina, southDakota, tennessee, texas, utah, vermont, virginia, washington, westVirginia, wisconsin, wyoming
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
    url(r'^alabama$', alabama),
    url(r'^alaska$', alaska),
    url(r'^arizona$', arizona),
    url(r'^arkansas$', arkansas),
    url(r'^california$', california),
    url(r'^colorado$', colorado),
    url(r'^connecticut$', connecticut),
    url(r'^delaware$', delaware),
    url(r'^districtofColumbia$', districtofColumbia),
    url(r'^florida$', florida),
    url(r'^georgia$', georgia),
    url(r'^hawaii$', hawaii),
    url(r'^idaho$', idaho),
    url(r'^illinois$', illinois),
    url(r'^indiana$', indiana),
    url(r'^iowa$', iowa),
    url(r'^kansas$', kansas),
    url(r'^kentucky$', kentucky),
    url(r'^louisiana$', louisiana),
    url(r'^maine$', maine),
    url(r'^maryland$', maryland),
    url(r'^massachusetts$', massachusetts),
    url(r'^michigan$', michigan),
    url(r'^minnesota$', minnesota),
    url(r'^mississippi$', mississippi),
    url(r'^missouri$', missouri),
    url(r'^montana$', montana),
    url(r'^nebraska$', nebraska),
    url(r'^nevada$', nevada),
    url(r'^newHampshire$', newHampshire),
    url(r'^newJersey$', newJersey),
    url(r'^newMexico$', newMexico),
    url(r'^newYork$', newYork),
    url(r'^northCarolina$', northCarolina),
    url(r'^northDakota$', northDakota),
    url(r'^ohio$', ohio),
    url(r'^oklahoma$', oklahoma),
    url(r'^oregon$', oregon),
    url(r'^pennsylvania$', pennsylvania),
    url(r'^rhodeIsland$', rhodeIsland),
    url(r'^southCarolina$', southCarolina),
    url(r'^southDakota$', southDakota),
    url(r'^tennessee$', tennessee),
    url(r'^texas$', texas),
    url(r'^utah$', utah),
    url(r'^vermont$', vermont),
    url(r'^virginia$', virginia),
    url(r'^washington$', washington),
    url(r'^westVirginia$', westVirginia),
    url(r'^wisconsin$', wisconsin),
    url(r'^wyoming$', wyoming),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
