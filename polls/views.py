from django.shortcuts import render, get_object_or_404
from .models import Election, Vote
from politicians.models import Politician
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F

def index(request):
   latest_election_list = Election.objects.order_by('-pub_date')[:10]
   context = {'latest_election_list': latest_election_list}
   return render(request, 'polls/index.html', context)

def detail(request, election_id):
   election = get_object_or_404(Election, pk=election_id)  
   return render(request, 'polls/detail.html', {'election': election})

def vote(request, election_id):
   election = get_object_or_404(Election, pk=election_id)
   vote = get_object_or_404(Vote, user_name=request.user.id, election=election_id)
   if vote.vote == 0:
      try:
         selected_politician = election.politician_set.get(pk=request.POST['politician'])
      except (KeyError, Politician.DoesNotExist):
         # Redisplay the question voting form.
         return render(request, 'polls/detail.html', {
              'election': election,
              'error_message': "You didn't select a politician.",
         })
      else:
         selected_politician.votes = F("votes") + 1
         selected_politician.save()
         return HttpResponseRedirect(reverse('polls:results', args=(election.id, )))
   else:
      return HttpResponseRedirect(reverse('polls:results', args=(election.id, )))

def results(request, election_id):
   election = get_object_or_404(Election, pk=election_id)
   vote = get_object_or_404(Vote, user_name=request.user.id, election=election_id)
   vote.vote = 1
   vote.save()
   return render(request, 'polls/results.html', {'election': election})