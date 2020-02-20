from django.urls import path
from django.views import debug
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.Index, name='index'),
    path('postlist/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)