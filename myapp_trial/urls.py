from django.urls import path
from myapp_trial import views
app_name="myapp_trail"

urlpatterns=[
                path('',views.index,name="index"),
                path('home',views.home,name="home"),
                path('fact1/<val>',views.fact1,name="fact1"),

]