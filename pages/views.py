from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class PageUpdateView(UpdateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = '__all__'

class PageDeleteView(DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('page-list')
