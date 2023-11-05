from django.urls import include, path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
    path('index', views.index, name = 'index'),
	path('view_course/<slug:course>', views.viewCourse, name = 'view_course'),
	path('login', views.login_user, name = 'login'),
	path('create_user', views.create_user, name = 'create_user'),
	path('logout', views.logout_user, name = 'logout'),
	path('select_major', views.select_major, name = 'select_major'),
    
    path('major', views.major, name = 'major')
]

app_name = 'cd'