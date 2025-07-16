from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageListView.as_view(), name='page-list'),
    path('create/', views.PageCreateView.as_view(), name='page-create'),
    path('<int:pk>/', views.PageDetailView.as_view(), name='page-detail'),
    path('<int:pk>/update/', views.PageUpdateView.as_view(), name='page-update'),
    path('<int:pk>/delete/', views.PageDeleteView.as_view(), name='page-delete'),
]
