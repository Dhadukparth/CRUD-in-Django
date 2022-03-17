from tkinter import messagebox
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from . models import user

# Create your views here.

def empty(request):
    return render(request, "index.html")

def display(request):
    data = user.objects.all()
    return render(request, "display.html",{"alldata" : data})

def update(request):
    return render(request, "update.html")

def delete(request):
    return render(request, "delete.html")

def signupForm(request):
    nm = request.POST["newName"]
    em = request.POST["newEmailid"]
    mo = request.POST["newMobile"]
    ps = request.POST["newPassword"]
    reps = request.POST["newRePassword"]

    if ps == reps:
        signup = user(name = nm, email = em, mobile = mo, password = ps)
        signup.save()
        return redirect(empty)

    else:
        messagebox.showerror("Error","Sorry!, This Password Is Not Matchs...")
        return redirect(empty)

def loginForm():
    em = request.POST["loginEmail"]
    ps = request.POST["loginPassword"]

    user.objects.get(email = em, password = ps)
    return redirect(empty)


def deleteForm(request):
    em = request.POST["deleteEmaiid"]
    ps = request.POST["deletePassword"]

    checkuser = user.objects.get(email = em, password = ps)
    checkuser.delete()
    return redirect(empty)        


def updateForm(request):
    em = request.POST["emailid"]
    nm = request.POST["updateName"]
    mo = request.POST["updateMobile"]
    ps = request.POST["updatePassword"]

    checkemail = user.objects.get(email=em)

    checkemail.name = nm
    checkemail.mobile = mo
    checkemail.password = ps
    checkemail.save()

    return redirect(display)