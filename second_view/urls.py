from django.urls import path, include, re_path

from second_view import views

urlpatterns = [
    re_path('view/\d{3}/',views.view_test1),
    re_path('view/\d{2,5}/\w+/',views.view_test2),
    re_path(r'^view/\d{6}/\w+/$',views.view_test3),

    path('views/',include([
        path('vip1/',views.view_vip1),
        path('vip2/',views.view_vip2),
        path('vip3/',views.view_vip3),
    ])),

    path('argument/',include([
        path('goto_page/',views.goto_page),
        path('argument/',views.argument),
    ])),
]