from django.test import TestCase
from . import models
# Question 객체 100개 생성
# 장고 앱 프레임으ㅏㄱㅇ,ㄹ py를 바로 실행할 수 있게

def main():
    for i in range(100):
        models.Question(
            subject=f'질문 {i}',
            content =f'질문 내용 {i}').save()
        
if __main___ == '__main__':
    main()
