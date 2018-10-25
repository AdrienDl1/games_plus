from django.urls import urls, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from games_review import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('games_review.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = 'games_review'
urlpatterns = [
    path('', views.index, name='index'),
    path('jeu/<slug:slug>', views.game, name='game'),
]
