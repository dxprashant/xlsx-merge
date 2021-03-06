import sys
import os
# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import render
import datetime
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from uploader.models import Document
from django.bin.formProject.uploader.forms import DocumentForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('uploader.views.list'))
    else:
        form = DocumentForm() # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.order_by('-id')[:5]

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request) )

    
    
    
    


        
        
        
        
