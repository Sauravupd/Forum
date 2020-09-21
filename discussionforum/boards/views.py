from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Board

# Create your views here.
def home(request,*args, **kwargs):
    board=Board.objects.all()
    my_context={'board':board}
    return render(request,'home.html',my_context)

def board_topics(request,id):
    try:
        board=get_object_or_404(Board,id=id)
    except Board.DoesNotExist:
        raise Http404
    return render(request,'topics.html',{'board':board})
