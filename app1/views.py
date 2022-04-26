import django.http
from app1.models import Ustoz, Fan, Yonalish
from django.shortcuts import render, redirect, HttpResponse

def salomlash(request):
    return render(request, {"ism":Akmal})

def asosiy(request):
    return render(request, "asosiy.html")



def Ustoz(request):
    a = Ustoz.objects.all()
    if request.method == 'POST':
        a = request.POST.get("a")
        ustoz = Ustoz.objects.get(id=a)
        Fan.objects.create(
            ism=request.POST.get("i"),
            familiya=request.POST.get("f"),
            daraja=request.POST.get("d"),
        )
        return redirect("/ustoz/")
    mod = request.GET.get("Qidirish")
    if mod == None:
        u = Ustoz.objects.all().order_by("ism")
    else:
        u = Ustoz.objects.filter(ism=mod)
    return render(request, "Ustoz.html", {"ust":u})

def ustoz_edit(request, pk):
    if request.method == 'POST':
        u1 = Ustoz.objects.get(id=pk)
        u1.ism=request.POST.get("ismi")
        u1.familiya=request.POST.get("f")
        u1.daraja=request.POST.get("d")
        u1.save()
        return redirect("/ustozlar")
    u = Ustoz.objects.get(id=pk)
    return render(request, "ustoz-edit.html", {"ustoz":u})

def ust_ochir(request, son):
    Ustoz.objects.get(id=son).delete()
    return redirect("/ustozlar")



def fanlar(request):
    u = Ustoz.objects.all()
    if request.method == 'POST':
        u = request.POST.get("u")
        ustoz = Ustoz.objects.get(id=u)
        Fan.objects.create(
            nom=request.POST.get("n"),
            ustoz=ustoz,
        )
    soz = request.GET.get("qidirish")
    if soz == None:
        hammasi = Fan.objects.all().order_by("nom")
    else:
        hammasi = Fan.objects.filter(nom=soz)
    return render(request, "Fan.html", {"fanlar":hammasi,"ust":u})

def science_edit(request, op):
    if request.method == 'POST':
        a1 = Fan.objects.get(id=op)
        a1.nom=request.POST.get("n")
        a1.save()
        return redirect("fanlar")
    a = Fan.objects.get(id=op)
    return render(request, "science-edit.html", {"fan":a})

def fan_ochir(request, son):
    Fan.objects.get(id=son).delete()
    return redirect("/fanlar/")

def yonalish(request):
    if request.method == 'POST':
        if request.POST.get("i_a") == "False":
            qaytarish = False
        else:
            qaytarish = True
        Yonalish.objects.create(
            nom=request.POST.get("nomi"),
            code=request.POST.get("code"),
            start_date=request.POST.get("s_d"),
            is_active=qaytarish
        )
    db = request.GET.get("qidirish")
    if db == None:
        hamma = Yonalish.objects.all().order_by("nom")
    else:
        hamma = Yonalish.objects.filter(nom=db)
    return render(request, "yonalish.html", {"yonalish":hamma})

def yonalish_edit(request, ad):
    if request.method == 'POST':
        y1 = Yonalish.objects.get(id=ad)
        y1.nom=request.POST.get("nomi")
        y1.code=request.POST.get("code")
        y1.start_date.POST.get("s_d")
        y1.save()
        return redirect("/yonalishlar")
    y = Yonalish.objects.get(id=ad)
    return render(request, "yonalish-edit.html", {"yonalish":y})

def yn_ochir(request, son):
    Yonalish.objects.get(id=son).delete()
    return redirect("/yonalish")

