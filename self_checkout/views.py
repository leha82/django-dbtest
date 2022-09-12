from contextlib import nullcontext
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import TestData
from django.utils import timezone

def getHttpTemplete(selectedData, nameData=''):
    test = 1
    tableData=''
    for sd in selectedData:
        tableData += f'''
        <tr>
            <td>{sd.id}</td>
            <td>{sd.name}</td>
            <td>{sd.timestamp}</td>
            <td>{sd.detail}</td>
        </tr>
        '''

    article = f'''
    <html>
    <head></head>
    <body>
        <h2>Welcome</h2>
        Hello, Django
        <form action="/search/" method="post">
        <div>
            <p><input type="text" name="name">
            <input type="submit" value="search"></p>
        </div>
        </form>
        <form action="/insert/" method="post">
        <div>
            <p><input type="text" name="id">
            <input type="text" name="name">
            <textarea name="detail"></textarea>
            <input type="submit" value="insert"></p>
        </div>
        </form>
        <table border="1">
            <tr>
                <th>id</th>
                <th>name</th>
                <th>timestamp</th>
                <th>detail</th>
            </tr>
            {tableData}
        </table>
    </body></html>
    '''
    return article


# Create your views here.
@csrf_exempt
def index(request):
    selectedData = TestData.objects.all()
    # read selectdata and make array
    
    return HttpResponse(getHttpTemplete(selectedData))

@csrf_exempt
def insert(request):
    
    insertData = TestData()

    if request.method == 'POST':
        insertData.id = request.POST['id']
        insertData.name = request.POST['name']
        # insertData.timestamp = timezone.localtime()
        insertData.detail = request.POST['detail']

    a = insertData.save()
    print("*** 에러 ??? : ",a)
    return redirect('/')

@csrf_exempt
def searchName(request):
    sname = ''
    if request.method == 'POST':
        sname=request.POST['name']
    if sname == '' or sname == None:
        return redirect('/')
    selectedData = TestData.objects.filter(name=sname)
    return HttpResponse(getHttpTemplete(selectedData,sname))


