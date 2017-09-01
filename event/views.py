from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Event
from .forms import EventEditForm


# Create your views here.
def index(request):
    return render(request, 'event/index.html')

class EventView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'event/event_views.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        return super().get_queryset().filter(author__pk = self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = EventEditForm()
        context.update({
            'form': form
        })
        return context


@login_required
def done(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    event.has_done = True
    event.save()
    messages.info(request,'You have finished the plan.')
    form = EventEditForm()
    context = {
        'event_list': Event.objects.all(),
        'form': form,
    }

    return render(request, 'event/event_views.html', context=context)

@login_required
def delete(request, event_pk):
    get_object_or_404(Event, pk=event_pk)
    Event.objects.filter(pk=event_pk).delete()
    messages.info(request, 'You have deleted the pan.')
    form = EventEditForm()
    context = {
        'event_list': Event.objects.all(),
        'form': form,
    }
    return render(request,'event/event_views.html', context=context)


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'event/detail_event.html'
    context_object_name = 'event'

@login_required
def post_plan(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    form = EventEditForm(request.POST)
    if form.is_valid():
        plan = form.save(commit=False)
        plan.author = user
        plan.save()
    else:
        messages.warning(request, "Something is ERROR.")
    return redirect(reverse('event:events', args=(user_pk,)))
