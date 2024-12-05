from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from .models import subject
from django.urls import reverse_lazy
class Showdata(ListView):
    model = subject
    template_name = "Show.html"
    context_object_name = "subject"
    fields = ["Course_id","Course_name","Teacher_name"]

    def get_queryset(self):
        queryset =  super().get_queryset()
        query = self.request.GET.get("search",'')

        if query:
            queryset = queryset.filter(Course_name__icontains=query)
        return queryset

class Edit(UpdateView):
    model = subject
    template_name = "update.html"
    fields = ["Course_name","Teacher_name"]
    success_url = reverse_lazy("Show")

class Del(DeleteView):
    model = subject
    template_name = "del.html"
    fields = ["Course_name","Teacher_name"]
    success_url = reverse_lazy("Show")