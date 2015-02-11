import pyexcel.ext.xlsx
import glob
import shutil
from datetime import datetime
from time import gmtime, strftime
import os
from uploader.models import Document
from django.bin.formProject.uploader.forms import DocumentForm

def Merge():
    n=strftime('%H%M%S',gmtime())
    merged=pyexcel.Sheet()
    for file in glob.glob('c:\\python34\\lib\\site-packages\\django\\bin\\formProject\\media\\documents\\*.xlsx'):
        merged.row+=pyexcel.Reader(file)
    writer=pyexcel.Writer('c:\\python34\\lib\\site-packages\\django\\bin\\formProject\\media\\Merged\\a'+n+'.xlsx')
    writer.write_reader(merged)
    writer.close()
    
def WorkBook():
    from pyexcel.cookbook import merge_all_to_a_book
    merge_all_to_a_book(glob.glob('c:\\python34\\lib\\site-packages\\django\\bin\\formProject\\media\\Merged\\*.xlsx'),'c:\\python34\\lib\\site-packages\\django\\bin\\formProject\\media\\Final\\final.xlsx')


def delete_folder1():
    shutil.rmtree('c:\\python34\\lib\\site-packages\\django\\bin\\formProject\\media\\documents')
    #mdel()

def delete_folder2():
    shutil.rmtree('c:\\python34\\lib\\site-packages\\django\\bin\\formProject\\media\\merged')
    os.mkdir('c:\\python34\\lib\\site-packages\\django\\bin\\formProject\\media\\merged')

    
def mdel():
    Document.objects.delete()
    
    
