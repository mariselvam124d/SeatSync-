from django.contrib import admin
from django.urls import path
from exams import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/admin_allocation/', views.admin_allocation, name='admin_allocation'),  # ✅ updated path
    path('student/student_allocation/', views.student_allocation, name='student_allocation'), 
    path('student/student_allocation/result/', views.student_allocation_result, name='student_allocation_result'),
    # /student/allocation/
    path('staff/allocation/success/', views.allocation_success, name='allocation_success'),
    path('', views.home, name='home'),
    path('home/index/', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


