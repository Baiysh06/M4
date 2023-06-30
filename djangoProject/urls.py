from django.contrib import admin
from django.urls import path
from product.views import hello, time, goodby

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/' , hello),
    path('time/', time),
    path('goodby/', goodby)
]
