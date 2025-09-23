from django.shortcuts import render
from .forms import BetslipForm

# Create your views here.
def submit_slip(request):
    if request.method == 'POST':
        form = BetslipForm(request.POST)
        if form.is_valid():
            slip = form.save(commit=False)
            slip.status = 'checked'  # Default status

            slip.save()
            return render(request, 'slips/results.html', {'slip': slip})
    else:
        form = BetslipForm()
    return render(request, 'slips/submit.html', {'form': form})
