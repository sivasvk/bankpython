from django.shortcuts import render


def demo(request):
    return render(request,"home.html")