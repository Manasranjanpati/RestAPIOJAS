from AuthApp.models import AssetData
from rest_framework import serializers



def asset_price(asset_price):
    if asset_price >= 2000:
        return asset_price
    else:
        raise serializers.ValidationError("The Amount is not Valid")

class AssetSerialzers(serializers.ModelSerializer):
    asset_price = serializers.FloatField(validators=[asset_price])

    class Meta:
        model = AssetData
        fields = "__all__"
    
