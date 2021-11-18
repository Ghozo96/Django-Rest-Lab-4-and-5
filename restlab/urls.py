from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pintrest/movies/',include('pintrest.api.v1.urls')),
    path('accounts/', include('account.urls')),
]
