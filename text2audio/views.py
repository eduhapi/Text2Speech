from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from gtts import gTTS
from docx import Document
import os
from datetime import datetime
from django.conf import settings

def read_text_from_file(file_path):
    """Read text from a .txt, .docx, or .pdf file."""
    if file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            return file.read()
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        text = []
        for para in doc.paragraphs:
            text.append(para.text)
        return '\n'.join(text)
    elif file_path.endswith('.pdf'):
        # PDF handling code here (using libraries like PyMuPDF or PyPDF2)
        pass
    else:
        raise ValueError("Unsupported file format. Please use .txt, .docx, or .pdf files.")

def get_audio_file_name():
    """Generate an audio file name with the current date and time."""
    now = datetime.now()
    return now.strftime("convert_%d_%m_%Y_%H_%M_%S.mp3")

def upload_file(request):
    if request.method == 'POST' and 'document' in request.FILES:
        document = request.FILES['document']
        fs = FileSystemStorage()
        file_path = fs.save(document.name, document)
        full_file_path = os.path.join(settings.MEDIA_ROOT, file_path)
        
        try:
            text = read_text_from_file(full_file_path)
            tts = gTTS(text=text, lang='en', slow=False)
            audio_file = get_audio_file_name()
            audio_file_path = os.path.join(settings.MEDIA_ROOT, audio_file)
            tts.save(audio_file_path)
            
             # Correctly construct the audio file URL
            audio_file_url = os.path.join(settings.MEDIA_URL, audio_file).replace('\\', '/')
            return redirect(f'/success/?audio_file_url={audio_file_url}')  # Pass the URL to success view
        except Exception as e:
            return HttpResponse(f"Error processing file: {e}")
    
    
    return render(request, 'upload.html')

'''def success(request):
    audio_file = request.GET.get('audio_file', '')
    return render(request, 'success.html', {'audio_file': audio_file})'''

def success(request):
    audio_file_url = request.GET.get('audio_file_url', '')
    context = {
        'audio_file_url': audio_file_url,
        'MEDIA_URL': settings.MEDIA_URL
    }
    return render(request, 'success.html', context)
