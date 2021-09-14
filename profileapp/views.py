from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):  # 이미지와 메시지, 닉네임을 담은 날라온 폼 데이터가 form 에들어있음
        temp_profile = form.save(commit=False)  # 그 데이터를 임시로 저장. 실제 db에 저장하지 않고!
        # 우리가 보낸 세가지의 데이터는 있는데, user라는 데이터가 아직 없는 것. 그래서 만들어주자.
        temp_profile.user = self.request.user  # 요청을 보낸 당사자 유저로 유저 저장
        temp_profile.save()  # 그제서야 최종 저장!!!
        return super().form_valid(form)


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'
