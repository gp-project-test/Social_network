from django.shortcuts import render
from models import Users

# Create your views here.
def show_all_user (request):
    users_info = Users.objects.all()
    return render(request, 'show_all_users.html', {'users': users_info})
