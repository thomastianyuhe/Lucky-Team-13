from django.shortcuts import render

def main(request):
    response = {}
    return render(request, 'rango/main.html', response)