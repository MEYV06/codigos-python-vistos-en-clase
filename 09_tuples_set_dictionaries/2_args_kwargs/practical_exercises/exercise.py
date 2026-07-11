# TODO 1: crea una funcion collect_args que reciba *args y retorne args.
# Luego llama collect_args con "lapiz", "cuaderno" y "regla", y revisa collected_args.
def collect_args(*args):
    return args
collected_args = collect_args("lapiz", "cuaderno", "regla")
# TODO 2: crea una funcion sum_numbers que reciba *numbers y retorne la suma.
# Luego llama sum_numbers con 5, 10 y 15, y revisa total_sum.
def sum_numbers(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total
total_sum = sum_numbers(5, 10, 15)
# TODO 3: crea una funcion build_profile que reciba **kwargs y retorne kwargs.
# Luego llama build_profile con name="Ana", age=20 y course="Python", y revisa profile.
def build_profile(**kwargs):
    return kwargs
profile = build_profile(name="Ana", age=20, course="Python")
# TODO 4: obtiene name y course desde profile.
# Luego revisa el valor de profile_name y profile_course.
profile_name = profile["name"]
profile_course = profile["course"]
# TODO 5: crea una lista llamada items con "monitor", "teclado" y "mouse".
# Luego revisa el valor de items para ver la lista base.
items = ["monitor", "teclado", "mouse"]
# TODO 6: llama collect_args desempaquetando items con *.
# Luego revisa el valor de unpacked_items para ver los argumentos recibidos.
unpacked_items = collect_args(*items)
# TODO 7: crea un diccionario llamado profile_data con city="Lima" y active=True.
# Luego revisa el valor de profile_data para ver el diccionario base.
profile_data = {"city": "Lima", "active": True}
# TODO 8: llama build_profile desempaquetando profile_data con **.
# Luego revisa el valor de unpacked_profile para ver los argumentos por clave recibidos.
unpacked_profile = build_profile(**profile_data)
# TODO 9: crea una funcion describe_order que reciba customer, *items y **details.
# La funcion debe retornar customer, items y details.
# Luego llama describe_order con "Luis", "lapiz", "cuaderno", priority=True y paid=False.
# Revisa el valor de order.
def describe_order(customer, *items, **details):
    return customer, items, details
order = describe_order("Luis", "lapiz", "cuaderno", priority=True, paid=False)
# TODO 10: desempaqueta order en order_customer, order_items y order_details.
# Luego revisa el valor de order_customer, order_items y order_details.
order_customer, order_items, order_details = order
# TODO 11: obtiene la cantidad de productos del pedido usando len(order_items).
# Luego revisa el valor de item_count.
item_count = len(order_items)
# TODO 12: obtiene el valor de paid desde order_details.
# Luego revisa el valor de is_paid.
is_paid = order_details["paid"]
