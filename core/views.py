from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def home(request):
    return redirect("products")
