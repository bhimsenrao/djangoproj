
from django.contrib import admin
from django.urls import path
from DJApp1      import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewPage/',views.viewPage),
    path("hello/",views.hello),
    path("loadMe/",views.loadMe),
]
