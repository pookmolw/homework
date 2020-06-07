from django.contrib import admin
from django.urls import path
from testcase_app import views

urlpatterns = [
    # 用例管理
    path('',views.testcase_list),
    path('debug/',views.debug),
    path('assert/',views.assert_result),
    path('add_testcase/',views.add_testcase),
    path('edit_testcase/<int:tid>/',views.edit_testcase),
    path('delete_testcase/<int:tid>/',views.delete_testcase),
]
