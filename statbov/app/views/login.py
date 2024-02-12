from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView

from ..forms import LoginForm


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm


class LoginCreateView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        authenticate_user = authenticate(
            self.request,
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticate_user is not None:
            login(self.request, authenticate_user)
            # Após o usuário se autenticar, redireciona ele para o app
            return redirect(reverse('app'))

        # If the user is not authenticated, an error message is displayed.
        messages.error(self.request, 'Invalid credentials.')
        return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error in data validation.')
        return super().form_invalid(form)
