from django.shortcuts import render
from django.http import JsonResponse
import joblib
from .models import PredResults

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV,cross_val_score, StratifiedKFold, GridSearchCV
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from lightgbm import LGBMClassifier
from imblearn.over_sampling import SMOTE
from sklearn import metrics
from sklearn.svm import SVC


def index(request):
    return render(request, 'predict.html')


def predict(request):
    if request.POST.get('action') == 'post':

        # 데이터 입력값 받기
        username = request.POST.get('username')
        Total_Trans_Amt = float(request.POST.get('Total_trant_Amt'))
        Education_Level = float(request.POST.get('Edu_level'))
        Income_Category = float(request.POST.get('Income'))
        Total_Relationship_Count = float(request.POST.get('Total_relationship_cnt')) 
        Months_on_book = float(request.POST.get('Month_on_book')) 
        Customer_Age = float(request.POST.get('Customer_age')) 
        Contacts_Count_12_mon = float(request.POST.get('Contact_cnt_12'))
        Dependent_count = float(request.POST.get('Dependent_count')) 
        Gender = float(request.POST.get('gender')) 

        # model 가져오기
        model = joblib.load('churner/lgbm_model_w.pkl')
    
        # 예측 하기
        result = model.predict([[Total_Trans_Amt, Education_Level, Income_Category, Total_Relationship_Count, 
                                 Months_on_book, Customer_Age, Contacts_Count_12_mon, Dependent_count, Gender]])

        classification = result

        PredResults.objects.create(username=username,Total_Trans_Amt=Total_Trans_Amt, Education_Level=Education_Level, Income_Category=Income_Category,
                                   Total_Relationship_Count=Total_Relationship_Count, Months_on_book=Months_on_book,
                                   Customer_Age=Customer_Age, Contacts_Count_12_mon=Contacts_Count_12_mon, 
                                   Dependent_count=Dependent_count, Gender=Gender, result=classification)

        return JsonResponse({'username':username,'Total_Trans_Amt': Total_Trans_Amt, 'Education_Level': Education_Level, 'Income_Category': Income_Category,
                                   'Total_Relationship_Count': Total_Relationship_Count, 'Months_on_book':Months_on_book,
                                   'Customer_Age': Customer_Age, 'Contacts_Count_12_mon': Contacts_Count_12_mon, 
                                   'Dependent_count': Dependent_count, 'Gender': Gender, 'result':classification})


def view_results(request):
    data = {"dataset": PredResults.objects.all()}
    return render(request, "db.html", data)        