from django.urls import include, path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('view_course/<slug:course>', views.viewCourse, name = 'view_course'),
	path('login', views.login_user, name = 'login'),
	path('create_user', views.create_user, name = 'create_user'),
	path('logout', views.logout_user, name = 'logout')

]

app_name = 'cd'