from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('home/',views.home,name='home'),
    path('', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('add/',views.newJob,name="add"),
    path('del/<int:jid>',views.deleteJob,name="del"),
    path('done/<int:jid>',views.jobDone,name="done"),
    path('notdone/<int:jid>',views.notDone,name="ntfinished"),
    path('register/',views.register,name="register"),
]
