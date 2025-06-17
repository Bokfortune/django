from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='question_list'),  # board 앱의 index 뷰를 기본 URL로 설정
    path('<int:question_id>/', views.detail, name='question_detail'),  # 질문 상세 페이지 URL
]