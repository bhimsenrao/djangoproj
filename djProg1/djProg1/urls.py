
from django.contrib import admin
from django.urls import path
from  myapp1  import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.hello),
    path('test/',views.test),
    path('call/',views.call),
    path('myInfo/',views.myInfo),
    path('infoCall/',views.infoCall),
    
]
