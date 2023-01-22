from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from .views import HomePageView


urlpatterns = [
    path("admin/", admin.site.urls),
]



urlpatterns += [

path("", HomePageView.as_view(), name="home"),


]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
