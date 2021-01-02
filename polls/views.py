from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Poll, PollChoice

class NewPollForm(forms.Form):
    poll_title = forms.CharField(label='Poll Title')
    choice1 = forms.CharField(label='Choice')
    choice2 = forms.CharField(label='Choice')

# Create your views here.
def index(request):
    context = {
        'polls': Poll.objects.all(),
        'choices': PollChoice.objects.all()
    }
    return render(request, "polls/index.html", context)    

def new(request):
    if request.method == "POST":
        form = NewPollForm(request.POST)
        if form.is_valid():
           poll = Poll(
               len(master_polls),
               form.cleaned_data["poll_title"], [
                   PollChoice(0, form.cleaned_data["choice1"]),
                   PollChoice(1, form.cleaned_data["choice2"])
               ]
           )
           master_polls.append(poll)
           return HttpResponseRedirect(reverse("polls:index"))
    return render(request, "polls/new.html", {
        "form": NewPollForm()
    })