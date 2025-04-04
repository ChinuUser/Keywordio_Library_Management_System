from django.urls import path,include
from .views import sign_page_view,login_page_view,landing_page_view,student_page_view
from . import views
from .views import StudentList
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet



router = DefaultRouter()
router.register(r'students', StudentViewSet)

# Use the router in urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns=[
    path('login/',login_page_view),
    path("sign/",sign_page_view),
    path("",views.landing_page_view),
    path("student/",student_page_view),
    path('stud/', StudentList.as_view(), name='student-list'),
    path('', include(router.urls)),

]