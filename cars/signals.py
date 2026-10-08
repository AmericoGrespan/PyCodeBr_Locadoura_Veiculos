from django.db.models.signals import pre_save,  pre_delete, pre_save, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import tbl_carro, tbl_carsinventory 





def car_inventory_update():
    cars_count = tbl_carro.objects.all().count()
    cars_value = tbl_carro.objects.aggregate(
        total_value=Sum('value')  # <-- Usando Sum com 'S' maiúsculo
    )['total_value'] 

    tbl_carsinventory.objects.create(
        cars_count=cars_count, 
        cars_value=cars_value 
    )

@receiver(pre_save, sender=tbl_carro)
def car_pre_save(pre_save, instance,  **kwargs):
    if not instance.bios: 
           instance.bios = 'Bios Gerado Automaticamente  '



@receiver(pre_save, sender=tbl_carro)
def car_pre_save(sender, instance, **kwargs):
    print(instance)


@receiver(post_save, sender=tbl_carro)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(pre_delete, sender=tbl_carro)
def car_pre_delete(sender, instance, **kwargs):
    print('### PRE DELETE ###')
    print(instance)


@receiver(post_delete, sender=tbl_carro)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()