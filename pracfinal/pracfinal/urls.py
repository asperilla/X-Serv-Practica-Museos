"""pfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""


from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout, login
from django.views.static import serve


urlpatterns = [
	url(r'^$', 'museos.views.barra'),
	url(r'^museos$', 'museos.views.museos'),
	url(r'^museos/(\d+)$', 'museos.views.museo'),
	url(r'^logout', logout), 
	url(r'^login', login),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^about$', 'museos.views.about'),
 	url(r'^(.*)/xml$', 'museos.views.xml'),
	url(r'^(.*)$', 'museos.views.usuario'),
	url(r'static/(.*)$', serve, {'document_root': 'templates/Plantilla_1'}),
	url(r'static/(.*)$', serve, {'document_root': 'templates/Plantilla_museos'}),
	url(r'static/(.*)$', serve, {'document_root': 'templates/Plantilla_museo'}),
	url(r'static/(.*)$', serve, {'document_root': 'templates/Plantilla_personal'}),
	url(r'static/(.*)$', serve, {'document_root': 'templates/Plantilla_about'}),
	url(r'static/(.*)$', serve, {'document_root': 'templates/Plantilla_xml'}),
]
