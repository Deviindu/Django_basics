from django.shortcuts import render

def Student(request):
    return render(request,'student.html',
                {
                    "name":"indu",
                    "age":19,
                    "course":"Python FSD",
                    "college":"ISTS"
                }
            )