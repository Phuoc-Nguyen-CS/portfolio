from django.shortcuts import render
from projects.models import Project

def project_index(request):
    # Query (Create, Retrieve, Update, Delete Objects)
    # Returns a collection of all the objects that match the query
    projects = Project.objects.all()

    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):

    # Retrieves project with primary key (unique identifier of a database entry)
    project = Project.objects.get(pk=pk)
    context = {
        "project" : project
    }

    return render(request, "projects/project_detail.html", context)

def contact(request):
    return render(request, "projects/contact.html")