# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, render
from django.http import HttpResponse

# Create your views here.
from .forms import addform
from .models import queryapply

import os
import shutil

def index(request):
    if request.method == 'POST':

        form = addform(request.POST, request.FILES)

        if form.is_valid():
            busid = form.cleaned_data['busid']
            token = form.cleaned_data['token']
            usr_name = form.cleaned_data['usr_name']
            filepath = form.cleaned_data['filepath']
            aa = queryapply()
            aa.busid = busid
            aa.token = token
            aa.usr_name = usr_name
            aa.filepath = filepath
            aa.save()
            if len(os.listdir('tmpfiles/tmp')) > 1:
                return HttpResponse('上传失败，正在处理上批任务，请稍后！')
            else:
                f = open('tmpfiles/tmp/' + os.listdir('tmpfiles/tmp')[0])
                bb = f.read()
                f.close()
                bb = bb.split("\n")
                for file in os.listdir('tmpfiles/tmp'):
                    shutil.move(os.path.join('tmpfiles/tmp', file), 'tmpfiles/bac')               
                return render(request, 'home.html', {'bb': bb})
    else:
        form = addform()
    return render_to_response('index.html', {'form': form})
    


