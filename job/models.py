from django.db import models

# Create your models here.

class TJob(models.Model):
    companyName = models.CharField(max_length=50 )
    appliedOn = models.DateField( help_text="Please use the following format:  YYYY-MM-DD")
    source = models.CharField(max_length=50)
    jobId = models.CharField(max_length=50, blank=True)
    jobDesc = models.CharField(max_length=200, blank=True)
    statusLink = models.URLField(max_length=200,blank=True)
    ACCEPT  = "A"
    REJECT  = "R"
    UNKNOWN = "U"
    myChoice = (
        (ACCEPT,'accept'),
        (REJECT,"reject"),
        (UNKNOWN,"unknown")

    )

    result = models.CharField(max_length=1,choices=myChoice,default=UNKNOWN)


    def __str__(self):
        return self.companyName + " \nresult: " + str(self.result) + " \nappliedOn: " + str(self.appliedOn) + " \njobDesc: " +self.jobDesc