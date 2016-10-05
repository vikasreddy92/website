from django.shortcuts import render
from  django.http import HttpResponse, HttpRequest
from job.forms import TJobForm


# Create your views here.


def index(request):
    # return HttpResponse("job index view");
    myDict = {'boldmessage': "santhosh"}
    return render(request, 'job/index.html', context=myDict)


def addJob(request):
    if request.method == 'POST':
        form = TJobForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print(form.errors)
    else:
        form = TJobForm()

    return render(request, 'job/add_job.html', {'form': form})
