from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'super_people'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('update/<int:hero_id>/', views.update, name='update'),
    path('delete/<int:hero_id>/', views.delete, name='delete')
]# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
