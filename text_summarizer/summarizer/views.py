from django.shortcuts import render, redirect
from .forms import TextUploadForm
from .utils import summarize_text
from .models import UploadedText

def upload_text(request):
    if request.method == 'POST':
        form = TextUploadForm(request.POST)
        if form.is_valid():
            uploaded_text = form.save()
            summarized_text = summarize_text(uploaded_text.text)
            uploaded_text.summarized_text = summarized_text
            uploaded_text.save()
            pk=uploaded_text.pk
            uploaded_text = UploadedText.objects.get(pk=pk)
            return render(request, 'result.html', {'uploaded_text': uploaded_text})
            # return redirect('result', pk=uploaded_text.pk)
    else:
        form = TextUploadForm()
    return render(request, 'index.html', {'form': form})

def text_detail(request, pk):
    uploaded_text = UploadedText.objects.get(pk=pk)
    return render(request, 'result.html', {'uploaded_text': uploaded_text})