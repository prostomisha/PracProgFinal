from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:news_id>/', views.detail, name='detail'),
    path('create/', views.create),
    path('<int:news_id>/delete/', views.delete_news, name='delete'),
    path('<int:pk>/edit/', views.edit_news, name='edit'),
    path('category/<int:pk>/', views.listofcategories, name='listofcategories'),
    path('<int:news_id>/like/', views.likepost, name='like'),
    path('search/', views.search, name='search'),
]