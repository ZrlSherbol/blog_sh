from django.contrib import admin
from django.urls import path

from blog import settings
from posts.views import post_list, post_detail, main_view, post_create
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', post_list),
    path('post_create/', post_create),
    path('', main_view),
    path('posts/<int:post_id>/', post_detail)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
