from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User, Record
from django.contrib.auth.decorators import login_required
from django import forms
import json
from datetime import datetime
from django.core.paginator import Paginator
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

@login_required
def index(request):
    # get records based on the user id
    user_records = Record.objects.filter(user_id = request.user.id)
    print(user_records)
    if not user_records.exists():
        top = -1
        low = -1
    else:
        top = user_records.order_by('-date').first().date.year
        low = user_records.order_by('-date').last().date.year
    if request.method == "PUT":
        # get all yearly data
        data = json.loads(request.body)
        print(data.get("year"))
        records = Record.objects.filter(user_id = request.user.id, date__year = data.get("year"))
        print(records)
        print("all data")
        return JsonResponse({"records": [record.serialize() for record in records]}, safe=False)
    return render(request, "tracker/index.html", {
        "username": request.user.username,
        "top": top,
        "low": low
    })

# Yearly Summaries
@login_required
def yearly_summary(request):
    # get records based on the user id
    user_records = Record.objects.filter(user_id = request.user.id)
    print(user_records)
    if not user_records.exists():
        top = -1
        low = -1
    else:
        top = user_records.order_by('-date').first().date.year
        low = user_records.order_by('-date').last().date.year
    # default summary page will show the list of current month expenses
    if request.method == "PUT":
        data = json.loads(request.body)
        records = Record.objects.filter(user_id = request.user.id, date__year = data.get("year"))
        return JsonResponse({"records": [record.serialize() for record in records]}, safe=False)

    return render(request, "tracker/yearly_summary.html", {
        "top": top,
        "low": low
    })

# Monthly Summaries
@login_required
def monthly_summary(request):
    # get records based on the user id
    user_records = Record.objects.filter(user_id = request.user.id)
    print(user_records)
    if not user_records.exists():
        top = -1
        low = -1
    else:
        top = user_records.order_by('-date').first().date.year
        low = user_records.order_by('-date').last().date.year
        
    # default summary page will show the list of current month expenses
    if request.method == "PUT":
        data = json.loads(request.body)
        
        # load all records in the month
        if not data.get("edit") and data.get("load"):
            records = Record.objects.filter(user_id = request.user.id, date__year = data.get("year"), date__month = int(data.get("month"))).order_by('-date')
            return JsonResponse({"records": [record.serialize() for record in records]}, safe=False)
        # save edited record
        elif data.get("edit"):
            # retreive record object
            record = Record.objects.get(id = data.get("id"))
            
            # update values
            info = data.get("info")
            record.date = info[0]
            record.category = info[1]
            record.expense = info[2]
            record.location = info[3]
            record.memo = info[4]
    
            # save the record
            record.save()
            
            # send back a success message
            return JsonResponse({"message": "successfully saved data"})

    # delete existing record
    elif request.method == "DELETE":
        data = json.loads(request.body)
        Record.objects.get(id = data.get("id")).delete()
        return JsonResponse({"message": "successfully deleted"})    
    return render(request, "tracker/monthly_summary.html", {
        "top": top,
        "low": low
    })

@login_required
def record(request):
    # create a record
    if request.method == "POST":
        data = json.loads(request.body)
        
        for i in range(len(data["exp_arr"])):
            # create record
            i = Record.objects.create(
                user_id = request.user.id,
                date = data["date_all"],
                memo = data["memo_arr"][i],
                expense = data["exp_arr"][i],
                location = data["loc_arr"][i],
                category = data["cat_arr"][i]
            )
            # save record
            i.save()
        return JsonResponse({"message": "successfully saved"})
    
    return render(request, "tracker/record.html")
    
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "tracker/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "tracker/login.html")

def logout_view(request):
    logout(request)
    return render(request, "tracker/login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "tracker/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "tracker/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        # if already logged in, then just go to home page
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        # otherwise, register the user
        return render(request, "tracker/register.html")
