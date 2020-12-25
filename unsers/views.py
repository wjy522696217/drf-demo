from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json

class  studentView(View):
    def post(self,request):
        data = json.loads(request.body)
        print(data)

