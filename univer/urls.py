
from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = {
    path('admin/', admin.site.urls),
    path('', salomlash),
    path('asosiy/', asosiy),
    path('Ustoz/<int:son>', ust_ochir),
    path('ustoz-t/<int:pk>', ustoz_edit),
    path('Fan/<int:son>', fan_ochir),
    path('fanlar/<int:op>', science_edit),
    path('Yonalish/<int:ad>', yonalish_edit),
    path('yonalishlar/<int:son>', yn_ochir),
}
