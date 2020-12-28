from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

master_polls = []

class NewPollForm(forms.Form):
    poll_title = forms.CharField(label='Poll Title')
    choice1 = forms.CharField(label='Choice')
    choice2 = forms.CharField(label='Choice')
class PollChoice:
    def __init__(self, i, content):
        self.id = i
        self.content = content
        self.votes = 0
    
    def addVote(self):
        self.votes = self.votes + 1
class Poll:
    def __init__(self, i, title, choices):
        self.id = i
        self.title = title
        self.choices = choices

    def voteAt(self, index):
        self.choices[index].addVote()

# Create your views here.
def index(request):
    polls = master_polls
    context = {}
    if len(polls) > 0:
        for i in range(len(polls)):
            entry = {str(i): {"title": polls[i].title}}
            choices = {"choices": {}}
            for j in range(len(polls[i].choices)):
                choice = polls[i].choices[j]
                choices["choices"].update(
                    {str(j): {
                        "content": choice.content,
                        "votes": choice.votes
                    }
                })
            
            entry[str(i)].update(choices)
            context.update(entry)

    #context_final = {"polls": context}
    #print(context_final)
    return render(request, "polls/index.html", {
        "polls": context
    })    

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