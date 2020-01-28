import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import ProcessFormView

from label_ListPage.form import ticketChatForm
from label_ListPage.models import dashBourdBd as dashBourdBd, ticketChat

logger = logging.getLogger('django.dasBourd')
from django.http import HttpResponseRedirect


class dashBourd(LoginRequiredMixin, ListView):
    template_name = "label/dashBoard.html"
    model = dashBourdBd
    context_object_name = 'dash'


class ticketDetail(LoginRequiredMixin, DetailView, ProcessFormView):
    template_name = "label/ticketDetail.html"
    model = dashBourdBd
    model2 = ticketChat
    context_object_name = 'dash'
    form = ticketChatForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chat'] = self.model2.objects.filter(post=context['dash'].pk)

        if self.form.setF(context['dash'].pk, self.request.user.username):
            context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        forms = ticketChatForm(request.POST or None)
        if request.method == 'POST' and forms.is_valid():
            post = forms.cleaned_data.get("post", None)
            if self.get_object().pk == post:
                logger.warn(msg="Error invalid pk fields  form label_ListPage.chat \t user- {} \t article-- {}".format(
                    self.request.user, self.get_object()))
                return Http404("No valid forms")
            name = forms.cleaned_data.get("name", None)
            if self.request.user == name:
                logger.warn(
                    msg="Error invalid username fields  form label_ListPage.chat \t user- {} \t article-- {}".format(
                        self.request.user, self.get_object()))
                return Http404("No valid forms user")
            body = forms.cleaned_data.get("body", None)
            file = forms.cleaned_data.get("file", None)
            try:
                self.model2(post=self.get_object(), name=self.request.user, body=body, file=file).save()
            except:
                logger.error(
                    msg="Err Add row BD({}) in {},{} ".format(self.model, self.request.user, self.get_object()))
        return self.get(self.request)


class FormTicketCreate(LoginRequiredMixin, CreateView):
    model = dashBourdBd
    fields = ('title', 'content', 'File', 'types')
    template_name = "label/htmlForm/FormTicket.html"
    success_url = '/'

    def form_valid(self, form):
        """Valid form """
        if form.is_valid():
            title = form.cleaned_data.get("title", None)
            content = form.cleaned_data.get("content", None)
            file = form.cleaned_data.get("File", None)
            types = form.cleaned_data.get("types", None)
            autors = self.request.user

            self.model(title=title, content=content, File=file, types=types, autors=autors).save()
            return HttpResponseRedirect(self.success_url)


class FormTicketUpdate(LoginRequiredMixin, UpdateView):
    model = dashBourdBd
    template_name = "label/htmlForm/FormTicket.html"
    fields = ['title', 'content', 'autors', 'priority', 'types', 'status', 'File']
    success_url = '/'


class FormTicketDelete(LoginRequiredMixin, DeleteView):
    model = dashBourdBd
    success_url = '/'
    template_name = "label/htmlForm/FormTicket.html"
