from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('performance/', views.performance, name='performance'),
    path('stalls/', views.stall, name='stall'),
    path('activity/', views.activity, name='activity'),
    path('starred/', views.starred_list, name='starred_list'),
    path('star/<str:content_type>/<str:object_id>/', views.star_item, name='star_item'),
    path('search/', views.search_item, name='search_item'),
    path('feedback/', views.submit_feedback, name='submit_feedback'),  
    path('feedback/list/', views.feedback_list, name='feedback_list'),  
    path('feedback/update/<int:feedback_id>/', views.update_feedback, name='update_feedback'),  
    path('feedback/delete/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),  
    path('feedback/thanks/', views.feedback_thanks, name='feedback_thanks'),  
    path('profile/update/<int:client_id>/', views.update_profile, name='update_profile'),
]

