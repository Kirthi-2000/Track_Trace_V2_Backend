from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render

class Jig_Unloading_Main(APIView):
    def get(self, request):
        return render(request, 'Jig_Unloading/Jig_Unloading_Main.html')
    
    def post(self, request):
        return Response({"message": "POST request received"})

# Create your views here.
class JigUnloading_Completedtable(APIView):
    def get(self, request):
        return render(request, 'Jig_Unloading/JigUnloading_Completedtable.html')
    
class Nickel_Maintable(APIView):
    def get(self, request):
        return render(request, 'Jig_Unloading/Nickel_Maintable.html')