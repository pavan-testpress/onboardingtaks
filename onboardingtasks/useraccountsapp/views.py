from django.shortcuts import render
from django.views.generic import CreateView
from .models import UserAccounts
from .forms import CreateUserAccountsForm
# Create your views here.


class CreateUserAccounts(CreateView):
    model = UserAccounts
    form_class = CreateUserAccountsForm
    template_name = "useraccountsapp/usercreationform.html"

    def form_valid(self, form):
        print('saving..')
        form.user = self.request.user
        self.object = form.save()
        return super(CreateUserAccounts, self).form_valid(form)



