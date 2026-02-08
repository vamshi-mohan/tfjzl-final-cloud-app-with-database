from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Home / course list
    path('', views.CourseListView.as_view(), name='index'),

    # Auth
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    # Course details
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),

    # Enroll
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    
    path('<int:course_id>/submit/', views.submit, name='submit'),

    # SHOW HOW EXAM RESULT
    path(
        'course/<int:course_id>/submission/<int:submission_id>/result/',
        views.show_exam_result,
        name='exam_result'
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
