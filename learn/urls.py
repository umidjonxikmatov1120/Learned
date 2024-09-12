from django.urls import path

from learn.views import home_page_view, course_page_view, category_page_view, view_page_view

urlpatterns = [
    path('', home_page_view, name='home_page'),
    path('course/<str:slug>/', category_page_view, name='course_page'),
    path('gate/', course_page_view, name='gate_page'),
    path('view/<int:pk>/', view_page_view, name='view_page'),
]