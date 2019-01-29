from django.shortcuts import render, reverse, redirect,get_object_or_404
from django.urls import reverse_lazy

from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from poll.forms import PollForm, ChoiceForm
from django.views.generic import View
from poll.models import *
from django.utils.decorators import method_decorator
from employee_management_sys.decorator import *
# Create your views here.

class PollView(View):

    decorators = [login_required]

    @method_decorator(decorators)
    def get(self, request, id=None):
        if id:
            # qus = get_object_or_404(Qus, id)
            qus = Qus.objects.get(id=id)
            poll_form = PollForm(instance=qus)
            choices = qus.choices_set.all()
            choice_form = [ChoiceForm(prefix=str(
                choice.id), instance=choice) for choice in choices]
            template = 'poll/edit_poll.html'
        else:
            poll_form = PollForm(instance=Qus())
            choice_form = [ChoiceForm(prefix=str(x), instance=Choices()) for x in range(3)]
            template = 'poll/new_poll.html'
        context = {
            'poll_form':poll_form,
            'choice_form':choice_form
        }
        return render(request, template, context)

    @method_decorator(decorators)
    def post(self, request):
        context={}
        poll_form = PollForm(request.POST, instance=Qus())
        choice_form = [ChoiceForm(request.POST, prefix=str(x), instance=Choices()) for x in range(3)]
        if poll_form.is_valid() and all([cf.is_valid() for cf in choice_form]):
            new_poll = poll_form.save(commit=False)
            new_poll.created_by = request.user
            new_poll.save()
            for cf in choice_form:
                new_choice = cf.save(commit=False)
                new_choice.qus_id = new_poll
                new_choice.save()
            return HttpResponseRedirect('/polls/')
        context = {
            'poll_form': poll_form,
            'choice_form': choice_form
        }
        return render(request, 'poll/new_poll.html', context)

    @method_decorator(decorators)
    def put(self, request, id=None):
        context = {}
        qus = get_object_or_404(Qus, id)
        # qus = Qus.objects.get(id=id)
        poll_form = PollForm(request.POST, instance=Qus())
        choice_form = [ChoiceForm(request.POST, prefix=str(x), instance=Choices()) for x in range(3)]
        if poll_form.is_valid() and all([cf.is_valid() for cf in choice_form]):
            new_poll = poll_form.save(commit=False)
            new_poll.created_by = request.user
            new_poll.save()
            for cf in choice_form:
                new_choice = cf.save(commit=False)
                new_choice.qus_id = new_poll
                new_choice.save()
            return HttpResponseRedirect('/polls/')
        context = {
            'poll_form': poll_form,
            'choice_form': choice_form
        }
        return render(request, 'poll/new_poll.html', context)

    @method_decorator(decorators)
    def delete(self, request, id=None):
        pass

@login_required(login_url='/login/')
def index(request):
    qus = Qus.objects.all()
    context ={
        'question':qus,
        'title':'Polls'

    }
    return render(request, 'poll/index.html',context)

@login_required(login_url='/login/')
def details(request, id=None):
    context={}
    try:
        qus = Qus.objects.get(id=id)
    except:
        raise Http404
    context['qus'] = qus
    return render(request, 'poll/details.html', context)

@login_required(login_url='/login/')
def poll_delete(request, id=None):
    # qus_id = get_object_or_404(Qus, id)
    qus_id = Qus.objects.get(id=id)
    qus_id.delete()
    return redirect(reverse('index'))

@login_required(login_url='/login/')
def poll(request, id=None):
    if request.method=="GET":
        context={}
        try:
            qus = Qus.objects.get(id=id)
        except:
            raise Http404
        context['qus'] = qus
        return render(request, 'poll/poll.html', context)

    if request.method == "POST":
        data = request.POST
        user_id = 1
        print(data)
        res  = Answer.objects.create(user_id=user_id, choice_id=data['ans'])
        if res:
            return HttpResponse("Your vote is sucessfully saved.")
        else:
            return HttpResponse("Sorry, something is worng your vote is not saved")
