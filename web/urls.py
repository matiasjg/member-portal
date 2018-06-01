from django.urls import path,re_path

from . import views

app_name = 'web'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('members/<int:pk>/', views.DetailView.as_view(), name='member'),

    # ex: /members
    re_path(r'^members/$', views.ResultsView.as_view(), name='members'),

    # ex: /pay
    path('pay/', views.pay, name='pay'),

    # ex: /signup
    path('signup/', views.signup, name='signup'),

]
