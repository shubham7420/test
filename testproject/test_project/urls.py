from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    # === ProjectMaster ===
    path('projects/list/', views.project_list_page, name='project_list'),
    path('projects/add/', views.create_project, name='create_project'),
    path('projects/all/', views.get_all_projects, name='get_all_projects'),
    path('projects/<int:pk>/', views.get_project_by_id, name='get_project_by_id'),
    path('projects/<int:pk>/update/', views.update_project_by_id, name='update_project_by_id'),
    path('projects/<int:pk>/delete/', views.delete_project_by_id, name='delete_project_by_id'),

    # === ActivityMaster ===
    path('activities/list/', views.activity_list_page, name='activity_list'),
    path('activities/add/', views.create_activity, name='create_activity'),
    path('activities/all/', views.get_all_activities, name='get_all_activities'),
    path('activities/<int:pk>/', views.get_activity_by_id, name='get_activity_by_id'),
    path('activities/<int:pk>/update/', views.update_activity_by_id, name='update_activity_by_id'),
    path('activities/<int:pk>/delete/', views.delete_activity_by_id, name='delete_activity_by_id'),

    path('progress/all/', views.get_all_progress, name='get_all_progress'),
    path('progress/list/', views.progress_list_page, name='progress_list'),
    path('progress/add/', views.create_progress, name='create_progress'),
    path('progress/<int:pk>/', views.get_progress_by_id, name='get_progress_by_id'),
    path('progress/<int:pk>/update/', views.update_progress_by_id, name='update_progress_by_id'),
    path('progress/<int:pk>/delete/', views.delete_progress_by_id, name='delete_progress_by_id'),


    
]
