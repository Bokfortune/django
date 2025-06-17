from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answer


def index(request):
    question = Question.objects.order_by('-created_at') # 질문을 생성 시간 기준으로 내림차순
    return render(request, 'board/index.html', {'question': question})

# Create your views here.
