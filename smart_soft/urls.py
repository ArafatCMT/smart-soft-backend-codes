from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owners/', include('owners.urls')),
    path('products/', include('products.urls')),
    path('stocks/', include('stocks.urls')),
    path('peoples/', include('peoples.urls')),
    path('purchases/', include('purchases.urls')),
]
# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
