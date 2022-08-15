from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection

def home(request):
    # return HttpResponse("<h1> Welcome to About page </h1>")
    cursor=connection.cursor()
    cursor.execute("select * from post")
    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    print(posts)
    context={
        'keypost':posts
    }
    # third parameter should always be a dictionary
    return render(request,'Gunjanapp/home.html',context)

def create(request):
    return render(request,'Gunjanapp/form.html')

def insert(request):
    title = request.POST['blogTitle']
    content = request.POST['content']
    cursor = connection.cursor()
    cursor.execute("INSERT INTO post (`title`,`content`) VALUES ( %s, %s );", (title, content))
    cursor = connection.cursor()
    cursor.execute("SELECT * from post")
    print(request)
    return redirect('/gunjanapp/home')

# Create your views here.
