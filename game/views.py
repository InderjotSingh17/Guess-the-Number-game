from django.shortcuts import render, redirect
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100) 
        request.session['attempts'] = 0 

    return render(request, 'index.html')

def guess(request):
    if request.method == 'POST':
        user_guess = int(request.POST['guess'])
        request.session['attempts'] += 1
        number = request.session['number']
        if user_guess<number:
            message = "Too low! Try again."
        elif user_guess>number:
            message = "Too high! Try again."
        else:
            message = f"Congratulations! You guessed it in {request.session['attempts']} attempts."
            del request.session['number'] 
            del request.session['attempts']

        return render(request, 'index.html', {'message': message})

    return redirect('index')

