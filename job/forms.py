from job.models import  TJob
from django import forms

class TJobForm(forms.ModelForm):
    companyName = forms.CharField(max_length=50)
    appliedOn  = forms.DateField(help_text="Please use the following format:  YYYY-MM-DD")
    source = forms.CharField(max_length=50)
    jobId = forms.CharField(max_length=50)
    jobDesc = forms.CharField(max_length=200)
    statusLink = forms.URLField(max_length=200)
    result = forms.CharField(max_length=1)


    class Meta:
        model = TJob
        exclude = ()


