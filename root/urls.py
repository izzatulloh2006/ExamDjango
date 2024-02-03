from django.urls import path
from .views import todo_list, todo_create, todo_search_title, todo_filter_due, HomePageViews


urlpatterns = [
    path('',HomePageViews.as_view(), name='home'),
    path('todo/', todo_list, name='todo_list'),
    path('todo/create/', todo_create, name='todo_create'),
    path('todo/search/', todo_search_title, name='todo_search_title'),
    path('todo/filter/', todo_filter_due, name='todo_filter_due_date'),

]
