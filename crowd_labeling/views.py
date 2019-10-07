import random
from datetime import datetime

from django.conf import settings
from django.db.models import Count, Q
from django.shortcuts import render, redirect

from .forms import LabelStatementForm
from .models import Statement, Label, LabelChoices


def label(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    if request.method == 'POST':
        form = LabelStatementForm(request.POST)
        if form.is_valid():

            if request.POST.get('positive') is not None:
                statement_label = LabelChoices.POSITIVE
            else:
                statement_label = LabelChoices.NEGATIVE

            end_timestamp = datetime.now().timestamp()

            labeled_statement = Label(
                user=request.user,
                statement=Statement.objects.get(id=form.cleaned_data['statement_id']),
                answer_time=end_timestamp - form.cleaned_data['initial_timestamp'],
                label=statement_label
            )

            labeled_statement.save()

        return redirect('/label')
    else:
        statements = Statement.objects.annotate(label_count=Count('label')) \
            .filter(label_count__lte=settings.MAX_LABELS_PER_STATEMENT) \
            .filter(~Q(label__user__username=request.user.username))

        if len(statements) == 0:
            return render(request, 'complete.html', context={})

        statement = random.choice(statements)

        initial_timestamp = datetime.now().timestamp()
        form = LabelStatementForm(initial={
            'statement': statement.text,
            'statement_id': statement.id,
            'initial_timestamp': initial_timestamp,
        })
    return render(request, "label.html", context={"form": form})
