from django.db import models


class AssetData(models.Model):
    asset_no = models.IntegerField(primary_key=True)
    asset_name = models.CharField(max_length=100)
    asset_price = models.FloatField()
    asset_quantity = models.IntegerField()

