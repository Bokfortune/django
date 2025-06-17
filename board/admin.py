from django.contrib import admin

# Register your models here.

from .models import Question, Answer

# Question 모델을 관리자 사이트에 등록
# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('subject' ,) # 검색 기능을 위한 필드 설정

admin.site.register(Question,QuestionAdmin) # Qustion 모델과 QuestionAdmin을 연결