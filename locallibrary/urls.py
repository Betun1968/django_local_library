"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path

# Use static() to add url mapping to serve static files during development (only)
""" 
    Django no sirve ficheros estáticos como CSS, JavaScript e imágenes por defecto, pero puede ser útil para el 
    servidor web de desarrollo hacerlo así mientras creas tu sitio. Como adición final a este mapeador URL, 
    puedes habilitar el servicio de ficheros estáticos durante el desarrollo añadiendo las líneas siguientes.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),

    # urls del proyecto
   re_path(r'^catalog/', include('catalog.urls')),
   
   # mapea el url base (el del dominio) y lo redirige (RedirectView) hacia la aplicación
   # otra forma de hacerlo es con '' en path.
   path('', RedirectView.as_view(url='/catalog/', permanent=True)),

   # Permite utilizar el framework de authenticacion de django
   path('accounts/', include('django.contrib.auth.urls')),
   re_path('^accounts/login/$', include('django.contrib.auth.urls'), name='login'),
   re_path('^accounts/logout/$', include('django.contrib.auth.urls'), name='logout'),
   re_path('^accounts/password_change/$', include('django.contrib.auth.urls'), name='password_change'),
   re_path('^accounts/password_change/done/$', include('django.contrib.auth.urls'), name='password_change_done'),
   re_path('^accounts/password_reset/$', include('django.contrib.auth.urls'), name='password_reset'),
   re_path('^accounts/password_reset/done/$', include('django.contrib.auth.urls'), name='password_reset_done'),
   re_path('^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', include('django.contrib.auth.urls'), name='password_reset_confirm'),
   re_path('^accounts/reset/done/$', include('django.contrib.auth.urls'), name='password_reset_complete'),
   
]

# web estaticas durante el desarrollo
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)