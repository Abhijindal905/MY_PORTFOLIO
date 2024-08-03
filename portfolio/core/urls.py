from django.urls import path
from core import views
urlpatterns = [
    path("",views.home,name="home"),
    path('about/',views.about,name='about'),
    path('projects/',views.projects,name="projects"),
    path('certificates/', views.certificates,name="certificates"),
    path('resume/',views.resume,name="resume")

]
