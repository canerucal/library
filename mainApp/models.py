from django.db import models

# Create your models here.
class table_inventory(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_number = models.IntegerField()
    left_side = models.IntegerField()
    right_side = models.IntegerField()

    class Meta:
        db_table = 'table_inventory'

    def __str__(self) -> str:
        return f"{self.table_id} {self.table_number} {self.left_side} {self.right_side}"

class visitor(models.Model):
    visitor_id = models.AutoField(primary_key=True)
    visitor_name = models. CharField(max_length=20)
    visitor_surname = models. CharField(max_length=20)
    res_time = models.TimeField()

    class Meta:
        db_table = 'visitor'
    
    def __str__(self) -> str:
        return f"{self.visitor_id} {self.visitor_name} {self.visitor_surname} {self.res_time}"