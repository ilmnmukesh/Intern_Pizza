from API import models as API
from rest_framework import serializers
from bson.objectid import ObjectId
class PizzaTypeSerializer(serializers.Serializer):
    TYPE=(("Regular", "Regular"), ("Square", "Squaure"))
    name = serializers.ChoiceField(choices=TYPE)
    addPrice = serializers.FloatField()

class PizzaSizeSerializer(serializers.Serializer):
    SIZE = (
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large")
    )
    size = serializers.ChoiceField(choices=SIZE)
    addPrice = serializers.FloatField()

class PizzaSerializer(serializers.ModelSerializer):
    type = PizzaTypeSerializer(many=True)
    size = PizzaSizeSerializer(many=True)
    defaultTopping = serializers.PrimaryKeyRelatedField(queryset=API.Topping.objects.all(), many=True)

    class Meta:
        model = API.Pizza
        fields = "__all__"

    def create(self, validated_data):
        toppings = validated_data.pop("defaultTopping")
        obj = API.Pizza.objects.create(**validated_data)
        obj.defaultTopping.add(*toppings)            
        return obj

    def to_representation(self, instance):
        data =super().to_representation(instance)
        data["defaultTopping"]=[]
        for x in instance.defaultTopping.all():
            data["defaultTopping"].append(x.to_dict())
        return data

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = API.Topping
        fields= "__all__"


""""
from  API.serializer import PizzaSerializer as s
data={
    "type":[{"name":"Regular","addPrice":0}, {"name":"Square","addPrice":20}],
    "size":[{"size":"Small", "addPrice":0}, {"size":"Medium", "addPrice":35}, {"size":"Large", "addPrice":70}],
    "name":"cheesy",
    "price":120,
    "defaultTopping":[1, 2]
}

a=s(data=data)
a.is_valid()
a.errors
"""