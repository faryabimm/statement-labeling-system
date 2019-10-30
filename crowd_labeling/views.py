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
            end_timestamp = datetime.now().timestamp()
            statement_label = LabelChoices.NEUTRAL
            for choice_option in [x[1] for x in LabelChoices.values()]:
                if request.POST.get(choice_option) is not None:
                    statement_label = LabelChoices.value_of(choice_option)

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
            return render(request, 'complete.html', context={
                "notify": {
                    "type": "success",
                    "title": "Success",
                    "message": "Labeling finished. Thank You!"
                }
            })

        user_label_count = Label.objects.filter(user=request.user).count()
        max_possible_label_count = len(statements)
        statement = random.choice(statements)

        initial_timestamp = datetime.now().timestamp()
        form = LabelStatementForm(initial={
            'statement': statement.text,
            'statement_id': statement.id,
            'initial_timestamp': initial_timestamp,
        })
    return render(request, "label.html", context={
        "form": form,
        "user_label_count": user_label_count,
        "max_possible_label_count": max_possible_label_count,
        "progress_percentage": 100 * user_label_count / (user_label_count + max_possible_label_count),
    })


def complete(request):
    return render(request, 'complete.html', context={})
