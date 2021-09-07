from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()

        # 유저가 실제 요청 보낸 유저와 동일한 경우
        return func(request, *args, **kwargs)
    return decorated
