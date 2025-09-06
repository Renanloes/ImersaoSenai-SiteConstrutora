from django.shortcuts import render, redirect
from .forms import ColaboradorForm

def cadastro(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # redireciona para uma página de sucesso ou para a home
    else:
        form = ColaboradorForm()

    return render(request, 'index.html', {'form': form})
