from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:  # GET 등 post 를 제외한 나머지 메서드
        hello_world_list = HelloWorld.objects.all()
        return render(request,'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

class AccountCreateView(CreateView): # CreateView를 상속받는다.
    model = User # 장고에서 기본으로 제공헤주는 User라는 모델 사용!
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
