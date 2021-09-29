from django.urls import path
from . import views

urlpatterns=[
    path('',views.HomePageView.as_view(),name='home_page'),
    path('about/',views.AboutPageView.as_view(),name='about_page'),
    path('post_create/',views.PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/update/<int:pk>/',views.PostUpdateView.as_view(),name='post_update'),
    path('post/delete/<int:pk>/',views.PostDeleteView.as_view(),name='post_delete'),
]