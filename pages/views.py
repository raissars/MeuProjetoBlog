from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Page

class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'


class PageCreateView(CreateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = '__all__'

    def form_valid(self, form):
        messages.success(self.request, 'Página criada com sucesso!')
        return super().form_valid(form)


class PageUpdateView(UpdateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = '__all__'

    def form_valid(self, form):
        messages.success(self.request, 'Página atualizada com sucesso!')
        return super().form_valid(form)


class PageDeleteView(DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('page-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Página deletada com sucesso!')
        return super().delete(request, *args, **kwargs)
