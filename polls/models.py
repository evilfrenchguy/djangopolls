from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=200, default="Poll Title")

    def __str__(self):
        return self.title

class PollChoice(models.Model):
    content = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content