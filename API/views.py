from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . import serializer
from .models import Pizza, Topping
from bson.objectid import ObjectId
import csv
def loadCSV():
    data=[]
    with open("pizza.csv", "r") as s:
        for x in csv.DictReader(s):
            data.append(x)
    
    for x in data:
        if x["Veg"] == "FALSE":
            x["Veg"]=False
        else:
            x["Veg"]=True
    
    top=[]
    with open("topping.csv", "r") as s:
        for x in csv.DictReader(s):
            top.append(x)
            ser=serializer.ToppingSerializer(data=x)
            if ser.is_valid():
                ser.save()
            else:
                print(ser.errors)
    def a(s):
        return s.strip()
    for x in data:
        temp={
            "type":[{"name":"Regular","addPrice":0}, {"name":"Square","addPrice":30}],
            "size":[{"size":"Small", "addPrice":x["Small"]}, {"size":"Medium", "addPrice":x["Medium"]}, {"size":"Large", "addPrice":x["Large"]}],
            "name":x["Name"],
            "price":x["Base"],
            "defaultTopping":[]
        }
        for y in list(map(a,x["Topping"].split(","))):
            if y!="":
                obj=Topping.objects.get(name=y)
                temp["defaultTopping"].append(obj.id)
        ser=serializer.PizzaSerializer(data=temp)
        if ser.is_valid():
            ser.save()
        else:
            print(ser.errors)
    return top, data

def Pagenation(page):
    return (page-1)*10, page*10

@api_view([ "POST"])
def pizzaCreate(request):
    data={"success":False, "data":None,"errors":None }
    ser = serializer.PizzaSerializer(data=request.data)
    if ser.is_valid():
        obj= ser.save()
        data["success"]=True
        data["data"]=ser.to_representation(obj)
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        data["errors"]= ser.errors
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def pizzas(request):
    data={"success":True, "data":None,"errors":None }
    try:
        page=int(request.GET.get("page", 1))
    except:
        data["success"]=False
        data["errors"]="Bad Page request"
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    start, end = Pagenation(page)
    data["data"]= serializer.PizzaSerializer(instance=Pizza.objects.all()[start:end], many=True).data
    return Response(data,status=status.HTTP_200_OK)

@api_view(["POST", "DELETE"])
def pizzasEdit(request, id):
    data={"success":False, "data":None,"errors":None }
    try:
        obj=Pizza.objects.get(pk=ObjectId(id))
    except Pizza.DoesNotExist: 
        data["errors"]="Not available"
        return Response(data,status=status.HTTP_404_NOT_FOUND)
    except:
        data["errors"]="Bad request"
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='POST':
        ser=serializer.PizzaSerializer(obj,request.data)
        if ser.is_valid():
            obj=ser.save()
            data["data"]=ser.to_representation(obj)
            data["success"]= True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data["errors"]= ser.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    else:
        data["success"]=True
        data["data"]={
            "description":"%s delete successfully"%id
        }
        obj.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)

@api_view(["POST"])
def toppingCreate(request):
    data={"success":False, "data":None,"errors":None }
    ser = serializer.ToppingSerializer(data=request.data)
    if ser.is_valid():
        obj= ser.save()
        data["success"]=True
        data["data"]=ser.to_representation(obj)
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        data["errors"]= ser.errors
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET",])
def toppings(request):
    data={"success":True, "data":None,"errors":None }
    data["data"]= serializer.ToppingSerializer(instance=Topping.objects.all(), many=True).data
    return Response(data,status=status.HTTP_200_OK)


@api_view(["POST", "DELETE"])
def toppingsEdit(request, id):
    data={"success":False, "data":None,"errors":None }
    try:
        obj=Topping.objects.get(pk=id)
    except Topping.DoesNotExist: 
        data["errors"]="Not available"
        return Response(data,status=status.HTTP_404_NOT_FOUND)
    except :
        data["errors"]="Bad request"
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

    ser=serializer.ToppingSerializer(obj,request.data)
    if request.method=='POST':
        if ser.is_valid():
            obj=ser.save()
            data["data"]=ser.to_representation(obj)
            data["success"]= True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data["errors"]= ser.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    else:
        data["success"]=True
        data["data"]={
            "description":"%s delete successfully"%id
        }
        obj.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)