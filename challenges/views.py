from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month")

# def february(request):
#     return HttpResponse("Walk at least 20min every day")


monthly_challenges = {
    "January": "Eat no meat for the entire month",
    "February": "Walk at least 20min every day",
    "March": "Learn Django for at least 20min every day",
    "April": "Eat no meat for the entire month",
    "May": "Walk at least 20min every day",
    "June": "Learn Django for at least 20min every day",
    "July": "Eat no meat for the entire month",
    "August": "Walk at least 20min every day",
    "September": "Learn Django for at least 20min every day",
    "October": "Eat no meat for the entire month",
    "November": "Walk at least 20min every day",
    "December": "Learn Django for at least 20min every day",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path= reverse("month_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("This month is not supported")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
    
    # elif  month == "March":
    #     challenge_text = "Learn Django for at least 20min every day"
    # else:
    #     return HttpResponseNotFound("This month is not supported")
    
    # return HttpResponse(challenge_text)
    