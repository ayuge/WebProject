#!/usr/bin/env python
# encoding: utf-8
from django.urls import path

from polls import views


urlpatterns = [
    # .html模式(弃用)
    # path("polls/latest.html", views.index),

    # ex: /polls/
    path('', views.index, name='index'),

    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/result/
    path('<int:question_id>/results/', views.result, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]