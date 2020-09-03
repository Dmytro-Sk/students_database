from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    return render(request, 'students/students.html', {})


def students_add(request):
    return render(request, 'students/student_form.html')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete student %s</h1>' % sid)


def visiting_list(request):
    return render(request, 'students/visiting.html')


def classes_list(request):
    return render(request, 'students/classes.html')


def classes_add(request):
    return HttpResponse('<h1>Class add form</h1>')


def classes_edit(request, gid):
    return HttpResponse('<h1>Edit class %s</h1>' % gid)


def classes_delete(request, gid):
    return HttpResponse('<h1>delete class %s</h1>' % gid)

