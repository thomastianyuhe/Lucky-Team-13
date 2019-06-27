from django.shortcuts import render


def main(request):
    response = {}
    return render(request, 'rango/main.html', response)

def placePut(request):
    if request.method == 'POST':
        print("aaaa")#do stuff
    return render('rango/main.html', {})