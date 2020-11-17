from django.shortcuts import render
# Create your views here.
from django.template import RequestContext

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Document, Analyzedtext
from .forms import DocumentForm
from django.http import HttpResponse
import csv
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

try:
    import Image
except ImportError:
    from PIL import Image

global i, text
i = 0


global new_analyzed

def list(request):
    global i, text
    text = ""
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            iden = newdoc.docfile
            newdoc.save()

            i += 1
            #import ipdb;ipdb.set_trace()
            d = Document.objects.get(id=i)
            # print d.docfile
            # k = pytesseract.image_to_string(Image.open(d.docfile), lang="heb")
            k = pytesseract.image_to_string(Image.open(iden), lang="eng")
            #
            # from unidecode import unidecode
            # import pytesseract
            #
            # strs = pytesseract.image_to_string(Image.open('binarized_image.png'))
            # strs = unidecode(strs)
            # print(strs)
            #

            new_analyzed = Analyzedtext()
            new_analyzed.ana_text = k
            new_analyzed.save()
            text = new_analyzed.ana_text
            print(text)
            # print k

            # try:
            #     handle = open('data.txt', 'a+', encoding="utf-8")
            #     handle.write(k)
            #     handle.close()
            # except UnicodeDecodeError:
            #     if handle:
            #         handle.close()
            txt_file = r"data.txt"
            csv_file = r'mycsv.csv'

            in_txt = csv.reader(open(txt_file, "r", encoding="UTF-8"), delimiter=' ')
            out_csv = csv.writer(open(csv_file, 'w', encoding="UTF-8"))

            # out_csv.writerows(in_txt)

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    text = Analyzedtext()
    # Render list page with the documents and the form

    return render(request, 'list.html', {'documents': documents, 'form': form, "analyzed_text": text})
