from django.shortcuts import render
from django.template.loader import get_template
from .models import notes, comment
from .forms import add_notes, add_comment
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

def index(request):
	all_notes = notes.objects.all().order_by('-id')
	comments = comment.objects.all()

	form = add_notes()
	formtwo= add_comment()

	if request.method == 'POST' and 'form' in request.POST:
		form = add_notes(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path)

	elif request.method == 'POST' and 'formtwo' in request.POST:
		formtwo = add_comment(request.POST)

		if formtwo.is_valid():
			a = formtwo.cleaned_data['single_comment']
			b = request.POST.get('formtwo')
		
			comment.objects.create(note_id = int(b), single_comment=a)
		
			return HttpResponseRedirect(request.path)

	elif request.method == 'POST' and 'like' in request.POST:
		a = request.POST.get('like')
		likes = notes.objects.filter(title = a)
		total_likes = (likes[0].like)
		total_likes += 1
		notes.objects.filter(title=a).update(like = total_likes)
		return HttpResponseRedirect(request.path)

	elif request.method == 'POST' and 'dislike' in request.POST:
		a = request.POST.get('dislike')
		dislikes = notes.objects.filter(title = a)
		total_dislikes = (dislikes[0].dislike)
		total_dislikes += 1
		notes.objects.filter(title=a).update(dislike = total_dislikes)
		return HttpResponseRedirect(request.path)

	
		
	return render(request, 'main/index.html', context={'notes':all_notes, 'form':form, 'formtwo':formtwo, 'comments':comments})