from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.utils.timezone import make_naive

from webapp.models import Review
from .forms import ReviewForm, BROWSER_DATETIME_FORMAT


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = Review.objects.all()
    else:
        data = Review.objects.filter(status='moderated')
    return render(request, 'index.html', context={
        'reviews': data
    })


def review_view(request, pk):


    review = get_object_or_404(Review, pk=pk)

    context = {'review': review}
    return render(request, 'review_view.html', context)


def review_create_view(request):
    if request.method == "GET":
        form = ReviewForm()
        return render(request, 'review_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            # review = Review.objects.create(**form.cleaned_data)
            review = Review.objects.create(
                author=form.cleaned_data['author'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
                status=form.cleaned_data['status']
            )
            return redirect('review_view', pk=review.pk)
        else:
            return render(request, 'review_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def review_update_view(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "GET":
        form = ReviewForm(initial={
            'author': review.author,
            'email': review.email,
            'text': review.text,
            'status': review.status,
        })
        return render(request, 'review_update.html', context={
            'form': form,
            'review': review
        })
    elif request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            # Review.objects.filter(pk=pk).update(**form.cleaned_data)
            review.author = form.cleaned_data['author']
            review.email = form.cleaned_data['email']
            review.text = form.cleaned_data['text']
            review.status = form.cleaned_data['status']
            review.save()
            return redirect('review_view', pk=review.pk)
        else:
            return render(request, 'review_update.html', context={
                'review': review,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def review_delete_view(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'GET':
        return render(request, 'review_delete.html', context={'review': review})
    elif request.method == 'POST':
        review.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
