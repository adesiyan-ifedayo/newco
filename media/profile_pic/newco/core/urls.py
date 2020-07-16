from core import views
from django.urls import path
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
	path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/create/', views.profile_create_view, name='create'),
    path('profile/update/', views.profile_update, name='update'),
    path('journal/', views.journal_list_view, name='journal-list'),
    path('journal/<str:slug>/', views.journal_detail_view, name='journal-detail'),
    path('add_post/', views.journal_create_view),
    path('journal/<str:slug>/delete', views.journal_delete_view, name='journal-delete'),
    path('journal/<str:slug>/edit', views.journal_update_view, name='journal-update'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
