from django.shortcuts import render,get_object_or_404,redirect
from .models import Note
from .forms import NoteModelForm

def note_list_view(request):
    form = NoteModelForm()
    if request.method == "POST":
        form = NoteModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note-list')

    to_do_list = Note.objects.all().filter(finished=False)
    finished = Note.objects.all().filter(finished=True)
    context = {
        'to_do_list':to_do_list,
        'finished':finished,
        'form':form

    }
    return render(request,'note_list.html',context)



def finish_item(reuest,id):
    note = get_object_or_404(Note, id=id)
    note.finished = True
    note.save()
    return redirect('note-list')

def recover_item(reuest,id):
    note = get_object_or_404(Note, id=id)
    note.finished = False
    note.save()
    return redirect('note-list')


def delete_item(reuest,id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('note-list')
