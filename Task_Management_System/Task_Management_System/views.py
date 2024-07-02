from django.shortcuts import redirect

def home_redirect(request):
    return redirect('show_tasks')
