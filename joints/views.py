from django.shortcuts import render

from django.bin.formProject.joints.forms import EmailForm

from django.http import HttpResponse

from django.shortcuts import render_to_response

import os,tempfile,zipfile
from django.core.servers.basehttp import FileWrapper

from django.utils.encoding import smart_str

from django.core.files.base import ContentFile

import io

from django.conf.urls.static import static

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.bin.formProject.joints.newMerge import Merge
from django.bin.formProject.joints.newMerge import WorkBook
from django.bin.formProject.joints.newMerge import delete_folder1

import sys
from django.conf import settings
import mimetypes
from django.http import StreamingHttpResponse
import urllib
import re
from django.db import models



def download(request,file_name):
    file_path = settings.MEDIA_ROOT +'\\'+ file_name #added double \ instead of /
    file_wrapper = FileWrapper(open(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name) 
    return response

def home(request):
    if(request.GET.get('mybtn')):
        Merge()
        delete_folder1()
    return render_to_response('home.html', context_instance=RequestContext(request))
    
        
        
        


