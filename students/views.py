from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    students = [
        {
            'id': 1,
            'first_name': 'Віталій',
            'last_name': 'Подоба',
            'birthday': '02/05/2012',
            'image': 'students/1.jpg',
        },
        {
            'id': 2,
            'first_name': 'Корост',
            'last_name': 'Андрій',
            'birthday': '06/10/2012',
            'image': 'students/2.jpg',
        },
        {
            'id': 3,
            'first_name': 'Оришко',
            'last_name': 'Олег',
            'birthday': '03/12/2011',
            'image': 'students/default.png',
        },
    ]
    context = {'students': students}
    return render(request, 'students/students.html', context)


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

