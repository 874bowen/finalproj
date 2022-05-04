from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response

from .seralizers import StudentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated


class TestView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        qs = Student.objects.filter(id =1).first()
        seralizer = StudentSerializer(qs)
        return Response(seralizer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
