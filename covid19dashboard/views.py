from django.shortcuts import render


# View home page
def index(request):
    return render(request, 'dashboard/index.html')



