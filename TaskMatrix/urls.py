from django.contrib import admin
from django.urls import path, include
from tasks.views import home  # home 뷰를 임포트합니다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('작업/', include('tasks.urls')),
    path('', home, name='home'),  # 기본 URL에 대한 뷰를 추가합니다.
]
