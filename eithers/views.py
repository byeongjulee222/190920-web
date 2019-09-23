from IPython import embed
from django.shortcuts import render, redirect 
from .models import Question, Answer
# Create your views here.

def index(request):
    questions = Question.objects.order_by('-pk')
    context = {'questions': questions,}
    return render(request, 'eithers/index.html', context)

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        issue_a = request.POST.get('issue_a')
        issue_b = request.POST.get('issue_b')
        image_a = request.FILES.get('image_a')
        image_b = request.FILES.get('image_b')
        question = Question(title=title, issue_a=issue_a, issue_b=issue_b, image_a=image_a, image_b=image_b)
        question.save()
        return redirect('/eithers/') 
    else:
        return  render(request,'eithers/new.html')

def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk) 
    answers = question.answer_set.all()
    context = {'question': question, 'answers': answers,}
    return render(request, 'eithers/detail.html', context)


cnt0 = 0
cnt1 = 0
def answer_create(request, question_pk):
    global cnt0, cnt1
    question = Question.objects.get(pk=question_pk) 
    if request.method == 'POST':
        comment = request.POST.get('comment')
        pick = request.POST.get('pick')

        if pick == '0':
            cnt0 += 1
            result = (cnt0 // (cnt0 + cnt1)) * 100
        else:
            cnt1 += 1
            result2 = (cnt1 // (cnt0 + cnt1)) * 100
        answer = Answer(question=question, comment=comment, pick=pick) 
        answer.save()
        # print(result)
        context = {'question_pk': question_pk, 'result': result, 'result2': result2}
        return render(request, 'eithers/detail.html', context)

    else:
        return redirect(question)

def comment_delete(request, question_pk, answer_pk):
    answer = Answer.objects.get(pk=answer_pk)
    if request.method == 'POST':
        answer.delete()
    return redirect('eithers:detail', question_pk)

