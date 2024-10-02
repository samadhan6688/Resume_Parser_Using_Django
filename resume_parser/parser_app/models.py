from django.db import models

class ResumeData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    linkedin_link = models.URLField(blank=True, null=True)
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
