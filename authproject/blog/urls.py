from django.urls import path,include
from blog import views

app_name = "blog"

urlpatterns = [
    path('',views.listing),
    path('<int:blog_id>',views.detail,name = "blog_detail")
]

