from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from main.models import student
# Create your views here.
def inde(request):
    if(request.method=="POST"):
        return render(request,'2nd.html')
    return render(request,'index.html')
def home(request):
    return render(request, 'index.html')
def student_group(request):
    return render(request, '2nd.html')
def index(request):
    return render(request,'index1.html')
def gets(request):
    if request.method == "POST":
        stakeholder = request.POST.get('stakeholder')
        if stakeholder == 'student':
            name = request.POST.get('name_student')
            batch = request.POST.get('batch_stu')
            email = request.POST.get('email_stu')
            saves=student(name=name,email=email,batch=batch)
            saves.save()

            # Process the student data as needed
            # For example, you can save the data to the database
            # and prepare a success or error message

            # Assuming data processing is successful
            response_data = {"message": "Student data received and processed successfully"}

        elif stakeholder == 'staff':
            # Process staff data in a similar manner
            # ...
            staff_name=request.POST.get('staff_name')
            staff_email=request.POST.get('staff_email')
            response_data = {"message": " data received and processed successfully"}

        elif stakeholder == 'parent':
            # Process parent data in a similar manner
            # ...
            sd=request.POST.get('sd')
            batch=request.POST.get('batch')
            ocu=request.POST.get('occupation')
            response_data = {"message": " data received and processed successfully"}

        elif stakeholder == 'industry':
            sd=request.POST.get('idus_name')
            batch=request.POST.get('working_in')
            ocu=request.POST.get('designation')
            sd=request.POST.get('email_ind')
            batch=request.POST.get('uploads')
            response_data = {"message": " data received and processed successfully"}
        elif stakeholder == 'academician':
            name_c=request.POST.get('name_c')
            coll_ame=request.POST.get('name_coll')
            desig=request.POST.get('desig')
            id=request.POST.get('id')
            response_data = {"message": " data received and processed successfully"}
        elif stakeholder == 'alumni':
            name_al=request.POST.get('name_alumni')
            batch_al=request.POST.get('batchs')
            current=request.POST.get('curret')
            desigs=request.POST.get('desigs')
            response_data = {"message": " data received and processed successfully"}
        else:
            response_data = {"message": "Invalid stakeholder selected"}

        return JsonResponse(response_data)
    
    return render(request, '2nd.html')

