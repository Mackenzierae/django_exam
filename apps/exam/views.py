from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Wish, Added
from datetime import date

def index(request):
    return render(request, "exam/index.html")

def register(request):
    if request.method == "POST":
        date_hired = request.POST['date_hired']
        print date_hired
        form_errors = User.objects.validate_user_info(request.POST, date_hired)

        if len(form_errors) > 0:
            for error in form_errors:
                messages.error(request, error)
            print date_hired
        else:
            user = User.objects.register(request.POST)
            print user
            messages.success(request, "You have Successfully registered! Please sign-in to continue")

    return redirect('/')

def login(request):
    if request.method == "POST":
        user = User.objects.login(request.POST)
        if not user:
            messages.error(request, "Invalid login credentials!")
        else:
            request.session['logged_user'] = user.id
            return redirect('/dashboard')
    return redirect('/')


def dashboard(request):
    if "logged_user" not in request.session:
        messages.error(request, "Gotta login bro")
        return redirect('/')

    logged_user = User.objects.get(id=request.session['logged_user'])

    lu_created_wishes = Wish.objects.filter(wish_creator=logged_user)
    lu_added_wishes = Wish.objects.filter(added__wish_adder=logged_user)

    all_logged_user_wishes = lu_created_wishes | lu_added_wishes

    other_user_wishes = Wish.objects.exclude(id__in=all_logged_user_wishes)

    context = {
        'logged_user': logged_user,
        "all_logged_user_wishes": all_logged_user_wishes,
        'other_user_wishes': other_user_wishes,
    }


    return render(request, "exam/dashboard.html", context)

def add_wish_page(request):
    if "logged_user" not in request.session:
        messages.error(request, "Gotta login bro")
        return redirect('/')


    return render(request, "exam/add_wish.html")


def add_wish(request):
    if request.method == "POST":

        form_errors = Wish.objects.validate_wish(request.POST)

        logged_user = User.objects.get(id=request.session['logged_user'])
        if len(form_errors) > 0:
            for error in form_errors:
                messages.error(request, error)
            return redirect('/add_wish_page')
        else:
            logged_user = User.objects.get(id=request.session['logged_user'])
            create = Wish.objects.create(wish_creator=logged_user, item=request.POST['item'])
            print create
            return redirect('/dashboard')

def delete_wish(request, wish_id):

    wish = Wish.objects.get(id=wish_id).delete()

    return redirect('/dashboard')


def add_to_wishes(request, wish_id):

    logged_user = User.objects.get(id=request.session['logged_user'])
    wish = Wish.objects.get(id=wish_id)
    Added.objects.create(wish_adder=logged_user, wish=wish)

    return redirect('/dashboard')

def remove_wish(request, wish_id):

    logged_user = User.objects.get(id=request.session['logged_user'])
    wish = Wish.objects.get(id=wish_id)

    Added.objects.get(wish_adder=logged_user, wish=wish).delete()

    return redirect('/dashboard')






def wish_page(request, wish_id):
    if "logged_user" not in request.session:
        messages.error(request, "Gotta login bro")
        return redirect('/')
    wish = Wish.objects.get(id=wish_id)

    wish_adders = Added.objects.filter(wish_id=wish_id)

    context = {
        "wish": wish,
        "wish_adders": wish_adders,
    }

    return render(request, "exam/wish_page.html", context)



def logout(request):
    if 'logged_user' in request.session:
        request.session.pop('logged_user')
    return redirect('/')
