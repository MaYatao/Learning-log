"""定义learning_logs的URL模式"""

from django.conf.urls  import url
from . import  views
from django.urls import path

urlpatterns = [

    # Home page.
    path('', views.index, name='index'),
    # Show all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
     # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
     # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    #编辑主题
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    #删除条目
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    #删除主题
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),



    
    #url(r'^edit_topic/(?P<topic>\d+)$',views.edit_topic,name='edit_topic'),

   
    #主页
    #url(r'^$',views.index,name='index'),
    
    #显示所有主题
    #url(r'^topics/$',views.topics,name='topics'),

    #特定主题的详细页面
    #url(r'^topics/(?P<topic_id>\d+)$',views.topic,name='topic'),

    #用于添加新主题的网页
    #url(r'^new_topic/$',views.new_topic,name='new_topic'),

     #用于添加新条目的页面
    #url(r'^new_entry/(?P<topic_id>\d+)$',views.new_entry,name='new_entry'),

    #用于编辑条目的页面
    #url(r'^edit_entry/(?P<entry_id>\d+)$',views.edit_entry,name='edit_entry'),
  
]

app_name = 'learning_logs'