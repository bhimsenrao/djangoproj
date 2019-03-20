from django.contrib import admin
from django.urls import path
from myapp1      import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("viewer/",views.viewer),
    path('message/',views.message),
    path("dataForm/",views.dataForm),
    path("finalView/",views.finalView),
    path("sendData/",views.sendData),
    path("mydata/",views.mydata),
    path('setMySession/',views.setMySession),
    path('getMySession/',views.getMySession),
    path('clearMySession/',views.clearMySession),
    path('personIns/',views.personIns),
    path('saverec/',views.saverec),
    path('getAllRecords/',views.getAllRecords),
]
