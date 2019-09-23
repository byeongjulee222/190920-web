from django.urls import reverse
from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=20)
    issue_a = models.TextField()
    issue_b = models.TextField()
    image_a = models.ImageField(blank=True)
    image_b = models.ImageField(blank=True)

    def __str__(self):
        return self.title
        

    # def get_absolute_url(self):
    #     return reverse('eithers:detail', kwargs={'question_pk': self.pk})
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.CharField(max_length=200)

    class Meta:
        ordering = ['pk'] 

    def __str__(self):
        return self.comment
        # return f'<Article({self.question}): Comment({self.pk})-{self.content}'
