from django.urls import path
from django.views.generic import TemplateView
from contacts import views

urlpatterns = [
    # path("contact/", views.contact, name="contact"),
    # path("", TemplateView.as_view(template_name="contact.html"), name="contact"),
    path('', views.contact, name='contact'),
]