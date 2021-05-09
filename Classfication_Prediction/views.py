from django.shortcuts import render
from django.http import HttpResponse
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'loan-approval-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))


def home(request):
        return render(request,'index.html')


def predict(request):
    Property_Area_Semiurban=0
    if request.method == 'POST':

        applicant_Income = int(request.POST.get('applicant_Income'))
        coapplicant_Income = int(request.POST.get('coapplicant_Income'))
        dependents = int(request.POST.get('dependents'))
        loan_Amount = int(request.POST.get('loan_Amount'))
        loan_amount_term = int(request.POST.get('loan_amount_term'))


        Gender_Male = request.POST.get('Gender_Male')
        if(Gender_Male == 'Male'):
             Gender_Male = 1
        else:
             Gender_Male = 0     

        Married_Yes = request.POST.get('Married_Yes')
        if(Married_Yes == 'Yes'):
             Married_Yes = 1
        else:
             Married_Yes = 0

        Education_Graduate = request.POST.get('Education_Graduate')
        if(Education_Graduate == 'Graduate'):
             Education_Graduate = 1
        else:
             Education_Graduate = 0
             
        Self_Employed_Yes = request.POST.get('Self_Employed_Yes')
        if(Self_Employed_Yes == 'Yes'):
             Self_Employed_Yes = 1
        else:
             Self_Employed_Yes = 0
        
        Property_Area_Urban = request.POST.get('Property_Area_Urban')
        if(Property_Area_Urban == 'Urban'):
                Property_Area_Urban = 1
                Property_Area_Semiurban=0         
        elif(Property_Area_Urban == 'Semiurban'):
                Property_Area_Urban = 0
                Property_Area_Semiurban=1
        else:
                Property_Area_Urban = 0
                Property_Area_Semiurban=0

        data = np.array([[applicant_Income, coapplicant_Income, dependents, loan_Amount, loan_amount_term, Gender_Male, Married_Yes, Education_Graduate, Self_Employed_Yes, Property_Area_Urban, Property_Area_Semiurban]])
        my_prediction = (classifier.predict(data))
        context = {'prediction':my_prediction}
        return render(request,'result.html',context)

