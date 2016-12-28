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
# from nextup.views import home, successSignup, expansion, northWest, southWest, northCentral, southCentral, northEast, southEast, alabama, alaska, arizona, arizonaR1, arizonaR2, arkansas, california, californiaR1, californiaR2, californiaR3, colorado, coloradoR1, coloradoR2, connecticut, delaware, districtofColumbia, florida, georgia, hawaii, idaho, idahoR1, idahoR2, idahoR3, illinois, indiana, iowa, iowaR1, iowaR2, iowaR3, kansas, kentucky, louisiana, maine, maryland, massachusetts, michigan, minnesota, mississippi, missouri, montana, nebraska, nevada, newHampshire, newJersey, newMexico, newYork, northCarolina, northDakota, ohio, oklahoma, oregon, pennsylvania, rhodeIsland, southCarolina, southDakota, tennessee, texas, utah, vermont, virginia, washington, westVirginia, wisconsin, wyoming
from nextup.views import *
from authentication.views import login, signup, checkUserhandle, userProfile
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
    url(r'^alabamaR1$', alabamaR1),
    url(r'^alabamaR2$', alabamaR2),
    url(r'^alaska$', alaska),
    url(r'^arizona$', arizona),
    url(r'^arizonaR1$', arizonaR1),
    url(r'^arizonaR2$', arizonaR2),
    url(r'^arkansas$', arkansas),
    url(r'^arkansasR1$', arkansasR1),
    url(r'^arkansasR2$', arkansasR2),
    url(r'^california$', california),
    url(r'^californiaR1$', californiaR1),
    url(r'^californiaR2$', californiaR2),
    url(r'^californiaR3$', californiaR3),
    url(r'^colorado$', colorado),
    url(r'^coloradoR1$', coloradoR1),
    url(r'^coloradoR2$', coloradoR2),
    url(r'^connecticut$', connecticut),
    url(r'^delaware$', delaware),
    url(r'^districtofColumbia$', districtofColumbia),
    url(r'^florida$', florida),
    url(r'^floridaR1$', floridaR1),
    url(r'^floridaR2$', floridaR2),
    url(r'^floridaR3$', floridaR3),
    url(r'^georgia$', georgia),
    url(r'^georgiaR1$', georgiaR1),
    url(r'^georgiaR2$', georgiaR2),
    url(r'^hawaii$', hawaii),
    url(r'^idaho$', idaho),
    url(r'^idahoR1$', idahoR1),
    url(r'^idahoR2$', idahoR2),
    url(r'^idahoR3$', idahoR3),
    url(r'^illinois$', illinois),
    url(r'^indiana$', indiana),
    url(r'^iowa$', iowa),
    url(r'^iowaR1$', iowaR1),
    url(r'^iowaR2$', iowaR2),
    url(r'^iowaR3$', iowaR3),
    url(r'^kansas$', kansas),
    url(r'^kentucky$', kentucky),
    url(r'^louisiana$', louisiana),
    url(r'^maine$', maine),
    url(r'^maryland$', maryland),
    url(r'^massachusetts$', massachusetts),
    url(r'^massR1$', massachusettsR1),
    url(r'^massR2$', massachusettsR2),
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
    url(r'^newyorkR1$', newYorkR1),
    url(r'^newyorkR2$', newYorkR2),
    url(r'^newyorkR3$', newYorkR3),
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
    url(r'^texasR1$', texasR1),
    url(r'^texasR2$', texasR2),
    url(r'^texasR3$', texasR3),
    url(r'^utah$', utah),
    url(r'^vermont$', vermont),
    url(r'^virginia$', virginia),
    url(r'^washington$', washington),
    url(r'^westVirginia$', westVirginia),
    url(r'^wisconsin$', wisconsin),
    url(r'^wyoming$', wyoming),
    url(r'^profile-page$', userProfile),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
