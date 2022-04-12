from django.shortcuts import render, redirect
import joblib
from .models import CovidList

reloadCovidModel = joblib.load('./models/covid_svm.pkl')
symptoms_values = []

def index(request):
    return render(request, 'index.html')


def predictCovidDisease(request):
    print(request)
    list = ['bp', 'fever', 'drycough', 'sorethroat', 'runningnose', 'asthma', 'headache', 'heartdisease', 'diabetes', 'hypertension', 'fatigue', 'abroad', 'contact', 'attended', 'visited', 'fam']
    length = len(list)
    symptoms_values = []

    # Get all values of on checkboxes
    if request.method == 'POST':
        checked_symptoms = request.POST.getlist('checks')

    # Check if the list of symptoms exists in the checked boxes
    for i in range(length):
        if list[i] in checked_symptoms:
            symptoms_values.append(1)
        else:
            symptoms_values.append(0)

    new_input = [symptoms_values]
    predictedval = reloadCovidModel.predict(new_input)[0]

    #converting predicted val to the results name
    if(predictedval == 1):
        covidval = "positive"
    else:
        covidval = "negative"
    context = {'covidval': covidval, 'predictedval': predictedval, 'new_input':new_input}#but still recording the predicted val (0,1,2)

    # Save to database
    obj = CovidList()
    obj.BreathingProblem = new_input[0][0]
    obj.Fever = new_input[0][1]
    obj.DryCough = new_input[0][2]
    obj.Sorethroat = new_input[0][3]
    obj.RunningNose = new_input[0][4]
    obj.Asthma = new_input[0][5]
    obj.Headache = new_input[0][6]
    obj.HeartDisease = new_input[0][7]
    obj.Diabetes = new_input[0][8]
    obj.Hypertension = new_input[0][9]
    obj.Fatigue = new_input[0][10]
    obj.AbroadTravel = new_input[0][11]
    obj.ContactCovidPatient = new_input[0][12]
    obj.AttendedLargeGathering = new_input[0][13]
    obj.VisitedPublic = new_input[0][14]
    obj.FamilyWorkingPublic = new_input[0][15]
    obj.covid = predictedval
    obj.save()

    return render(request, 'index.html', context)