from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, related_name='projects', blank=True)
    image = models.FileField(upload_to="project_images/", blank=True)
    github_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title