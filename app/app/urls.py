from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    url(r'^', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^about/', 'app.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
