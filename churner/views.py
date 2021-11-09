from django.shortcuts import render
from django.http import JsonResponse
import joblib
from .models import PredResults


def index(request):
    return render(request, 'predict.html')

def predict(request):
    if request.POST.get('action') == 'post':

        # 데이터 입력값 받기
        Total_trant_Amt = int(request.POST.get('Total_trant_Amt'))
        Edu_level = int(request.POST.get('Edu_level'))
        Income = int(request.POST.get('Income')) 
        Total_relationship_cnt = int(request.POST.get('Total_relationship_cnt')) 
        Month_on_book = int(request.POST.get('Month_on_book')) 
        Customer_age = int(request.POST.get('Customer_age')) 
        Contact_cnt_12 = int(request.POST.get('Contact_cnt_12')) 
        Dependent_count = int(request.POST.get('Dependent_count')) 
        gender = int(request.POST.get('gender')) 

        # model 가져오기
        model = joblib.load('./lgbm_model.pkl')

        # 예측 하기
        result = model.predict([[Total_trant_Amt, Edu_level, Income, Total_relationship_cnt, 
                                 Month_on_book, Customer_age, Contact_cnt_12, Dependent_count, gender]])

        classification = result[0]

        PredResults.objects.create(Total_trant_Amt=Total_trant_Amt, Edu_level=Edu_level, Income=Income,
                                   Total_relationship_cnt=Total_relationship_cnt, Month_on_book=Month_on_book,
                                   Customer_age=Customer_age, Contact_cnt_12=Contact_cnt_12, 
                                   Dependent_count=Dependent_count, gender=gender, result=classification)

        return JsonResponse({'Total_trant_Amt': Total_trant_Amt, 'Edu_level': Edu_level, 'Income': Income,
                                   'Total_relationship_cnt': Total_relationship_cnt, 'Month_on_book':Month_on_book,
                                   'Customer_age': Customer_age, 'Contact_cnt_12': Contact_cnt_12, 
                                   'Dependent_count': Dependent_count, 'gender': gender, 'result':classification})


def view_results(request):
    data = {"dataset": PredResults.objects.all()}
    return render(request, "db.html", data)        