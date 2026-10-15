
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse


def google_site_verification(request):
    return HttpResponse(
        "google-site-verification: google450b9ec7d227b652.html",
        content_type="text/plain",
    )


def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        "Sitemap: https://davietech-innovations.onrender.com/sitemap.xml\n"
    )
    return HttpResponse(content, content_type="text/plain")


def sitemap_xml(request):
    content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://davietech-innovations.onrender.com/</loc>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://davietech-innovations.onrender.com/contact/</loc>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
</urlset>"""
    return HttpResponse(content, content_type="application/xml")


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('ai/', include('ai_assistant.urls')),

    path(
        'google450b9ec7d227b652.html',
        google_site_verification,
        name='google_site_verification',
    ),

    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap_xml, name='sitemap_xml'),
]
