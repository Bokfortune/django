from django.test import TestCase
from . import models
# Create your tests here.

class Make100(TestCase):
    def test_make_100(self):
        # Question 객체 100개 생성
        for i in range(100):
            models.Question(
                subject=f'질문 {i}',
                content =f'질문 내용 {i}').save()
            # 데이터 베이스에 저장된 Question 객체의 개수 확인
