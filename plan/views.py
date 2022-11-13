from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import *
from .serializers import *
# Create your views here.

class AllPlanAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)

    def post(self,request):
        plan = request.data
        serializer = PlanSerializer(data=plan)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

class PlanAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request, pk):
        plan = Plan.objects.get(id=pk)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)

    def delete(self,request,pk):
        plan = Plan.objects.get(id=pk)
        if Plan.objects.filter(id=pk, user=request.user):
            plan.delete()
            natija = {
            "Success": "Plan o'chirildi"}
            return Response(natija)
        return Response({"Error": "Plan Error"})


    def put(self,request, pk):
        plan = Plan.objects.get(id=pk)
        serializer = PlanSerializer(plan, data=request.data)
        if serializer.is_valid() and Plan.objects.filter(id=pk, user=request.user):
            serializer.save(user=request.user)
            natija = {
                "Success": serializer.data
            }
            return Response(natija)
        return Response({"Error": serializer.data})