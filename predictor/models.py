from django.db import models

class CovidList(models.Model):
    BreathingProblem = models.CharField(max_length=5)
    Fever = models.CharField(max_length=5)
    DryCough = models.CharField(max_length=5)
    Sorethroat = models.CharField(max_length=5)
    RunningNose = models.CharField(max_length=5)
    Asthma = models.CharField(max_length=5)
    Headache = models.CharField(max_length=5)
    HeartDisease = models.CharField(max_length=5)
    Diabetes = models.CharField(max_length=5)
    Hypertension = models.CharField(max_length=5)
    Fatigue = models.CharField(max_length=5)
    AbroadTravel = models.CharField(max_length=5)
    ContactCovidPatient = models.CharField(max_length=5)
    AttendedLargeGathering = models.CharField(max_length=5)
    VisitedPublic = models.CharField(max_length=5)
    FamilyWorkingPublic = models.CharField(max_length=5)
    covid = models.CharField(max_length=5)

    def __str__(self):
        return self.covid