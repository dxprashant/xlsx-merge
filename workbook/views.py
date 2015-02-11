from django.shortcuts import render

from django.bin.formProject.joints.forms import EmailForm

from django.http import HttpResponse

from django.shortcuts import render_to_response

import os,tempfile,zipfile
from django.core.servers.basehttp import FileWrapper

from django.utils.encoding import smart_str

from django.core.files.base import ContentFile

import io

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.bin.formProject.joints.newMerge import WorkBook
from django.bin.formProject.joints.newMerge import delete_folder2

import os
import sys
from django.conf import settings
import mimetypes
from django.http import StreamingHttpResponse


import urllib
import re
from django.http import HttpResponse
from django.conf import settings
from django.db import models



def home(request):
    if(request.GET.get('bbtn')):
        WorkBook()
        delete_folder2()
    return render_to_response('wb.html', context_instance=RequestContext(request))

    

