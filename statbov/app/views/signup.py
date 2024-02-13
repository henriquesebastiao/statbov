from django.contrib import messages
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView

from ..forms import SignupForm


class SignupView(FormView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.request.session['signup_form_data'] = form.cleaned_data
        return super().form_valid(form)


class UserCreateView(CreateView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        raise Http404

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(user.password)  # Salva a senha criptografada no db
        user.save()
        messages.success(self.request, 'Usuário criado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        if 'email' in form.errors and form.cleaned_data.get('email') is None:
            messages.error(self.request, form.errors['email'][0])
        elif (
            'password' in form.errors
            and form.cleaned_data.get('password') is None
        ):
            messages.error(self.request, form.errors['password'][0])
        else:
            messages.error(
                self.request, 'Erro ao criar usuário, tente novamente.'
            )
        return super().form_invalid(form)
