from django.shortcuts import render

def main(request):
    return render(request, 'market1c/main.html')