from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.login,name='login'),
   path('index/',views.home,name="home"),
   path('adminPanel/',views.adminPanel,name="adminPanel"),
   path('missed/',views.missed,name="missed"),
   path('update/',views.update,name="update"),
   path('logout/',views.user_logout,name="logout"),
   path('connected/',views.Connected,name="Connected"),
   path('register/',views.register,name="register"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



