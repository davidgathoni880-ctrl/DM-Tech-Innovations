
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse


def google_site_verification(request):
    return HttpResponse(
        "google-site-verification: google450b9ec7d227b652.html",
        content_type="text/plain",
    )


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('ai/', include('ai_assistant.urls')),

    path(
        'google450b9ec7d227b652.html',
        google_site_verification,
        name='google_site_verification',
    ),
]