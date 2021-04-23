from django.shortcuts import render, redirect, HttpResponse, get_object_or_404,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from base import models



# decorator to check if user is logedin
def login_require(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/admin/")
    return wrapper


# view for showing sent messages
@login_require
def contact_admin(request):
    context = {}
    context["messages"] = models.MailToAdmin.objects.order_by("-date")
    return render(request, "contact_admin.html", context)


# to modeify user's messages (delete, read, answer)
@login_require
def generate_message(request, id, generate="del"):
    obj = get_object_or_404(models.MailToAdmin, pk=id)
    if generate == "del":
        obj.delete()
    elif generate == "mark":
        print("into mark")
        obj.checked = True
        obj.save()
    elif generate == "answer":
        return answer(request, id);
    return redirect("contact_admin")


# answer form view
@login_require
def answer(request, id):
    error=False
    user = get_object_or_404(models.MailToAdmin, pk=id)
    obj = models.School_info.objects.first()
    
    if request.method=="POST":
        admin = obj.email
        to = user.email
        subject = request.POST.get("subject")
        mess = request.POST.get("message")
        try:
            send_mail(subject=subject, message=mess, from_email=settings.EMAIL_HOST_USER, recipient_list=[to], fail_silently=False)
        except:
            return HttpResponseRedirect("?error=True")
        return redirect("contact_admin")
    
    elif request.GET.get("error"):
        error=True

    context={ "obj": obj, "user": user, "error": error }
    return render(request, "admin_form.html", context)

    
