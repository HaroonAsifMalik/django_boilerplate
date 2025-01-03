from django.contrib import admin
from django.urls import include, path

api_v1_patterns=[
    path("accounts/", include("accounts.urls")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include((api_v1_patterns, "api_v1"), namespace="api_v1")),

]
