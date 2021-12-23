from django.shortcuts import render

def index(request):
    """The home page for meals planning.""" 
    
    return render(request,'meal_plans/index.html')
