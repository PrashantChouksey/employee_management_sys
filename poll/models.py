from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Qus(models.Model):

    title = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(default='inactive', max_length=10)
    created_by= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    start_date = models.DateTimeField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choices_set.all()


class Choices(models.Model):

    qus_id = models.ForeignKey(Qus, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    @property
    def count_answer(self):
        return self.answer_set.count()

class Answer(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choices, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name +" - "+ self.choice.text

