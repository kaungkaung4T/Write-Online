from django.shortcuts import render
from display.models import Write
from rest.serializer import WriteSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.

# POST man
class Resting(APIView):
    serializer_class = WriteSerializers
    def get(self, request):
        w = Write.objects.all()
        ws = WriteSerializers(w, many=True)
        return Response(ws.data)

    def post(self, request):
        ws = WriteSerializers(data=request.data)
        if ws.is_valid():
            ws.save()
            return Response(ws.data)
        return Response(ws.errors)

    def put(self, request, pk):
        w = Write.objects.get(id=pk)
        ws = WriteSerializers(w, data=request.data)
        if ws.is_valid():
            ws.save()
            return Response(ws.data)
        return Response(ws.errors)

    def delete(self, request, pk):
        w = Write.objects.get(id=pk)
        w.delete()
        success = {
            "success":"success"
        }
        return Response(data=success)


# default
@api_view(["GET"])
def display(request):
    w = Write.objects.all()
    ws = WriteSerializers(w, many=True)
    return Response(ws.data)


@api_view(["POST"])
def upload(request):
    ws = WriteSerializers(data=request.data)
    if ws.is_valid():
        ws.save()
        return Response(ws.data)
    return Response(ws.errors)


@api_view(["PUT"])
def update(request, pk):
    w = Write.objects.get(id=pk)
    ws = WriteSerializers(w, data=request.data)
    if ws.is_valid():
        ws.save()
        return Response(ws.data)
    return Response(ws.errors)


@api_view(["DELETE"])
def delete(request, pk):
    w = Write.objects.get(id=pk)
    w.delete()
    success = {
        "success":"success"
    }
    return Response(data=success)
