from django import forms

class ResumeUploadForm(forms.Form):
    pdf_file = forms.FileField()
