from django.views.generic import TemplateView
from django.views import generic


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class UserDetailView(generic.DetailView):
    template_name = "pages/about.html"
