# TODO 1: crea una lambda sin parametros que devuelva "Reporte de productos".
get_title = lambda: "Reporte de productos"
# TODO 2: llama get_title() y guarda el resultado en title.
# Luego revisa el valor de title para ver el texto devuelto por la lambda.
title = get_title()
# TODO 3: crea una lambda que calcule el cuadrado de un numero.
square = lambda x: x**2
# TODO 4: llama square con 5 y guarda el resultado en square_result.
# Luego revisa el valor de square_result para ver el cuadrado de 5.
square_result = square(5)
# TODO 5: crea una lambda que calcule el subtotal usando precio y cantidad.
calculate_subtotal = lambda precio, cantidad: precio * cantidad
# TODO 6: llama calculate_subtotal con precio 20 y cantidad 3.
# Luego revisa el valor de subtotal para ver el resultado.
subtotal = calculate_subtotal(20, 3)
# TODO 7: crea una lambda que aplique 10% de descuento a un precio.
apply_discount = lambda precio: precio * 0.9
# TODO 8: llama apply_discount con 100 y guarda el resultado en discounted_price.
# Luego revisa el valor de discounted_price para ver el precio con descuento.
discounted_price = apply_discount(100)
# TODO 9: crea una lambda que devuelva "Caro" si el precio es mayor o igual a 100.
# Si no, debe devolver "Economico".
classify_price = lambda precio: "Caro" if precio >= 100 else "Economico"
# TODO 10: llama classify_price con 120 y guarda el resultado en price_category.
# Luego revisa el valor de price_category para ver la categoria del precio.
price_category = classify_price(120)
# TODO 11: crea una lista de precios.
# Luego revisa el valor de prices para ver la lista base.
prices = [50, 120, 250, 80, 100]
# TODO 12: crea una lambda que reciba una lista y devuelva solo precios mayores o iguales a 100.
get_high_prices = lambda lst: [p for p in lst if p >= 100]
# TODO 13: llama get_high_prices con prices y guarda el resultado en high_prices.
# Luego revisa el valor de high_prices para ver los precios filtrados.
high_prices = get_high_prices(prices)
# TODO 14: crea una lambda que reciba una lista y devuelva todos los precios con 10% de descuento.
get_discounted_prices = lambda lst: [p * 0.9 for p in lst]
# TODO 15: llama get_discounted_prices con prices y guarda el resultado en discounted_prices.
# Luego revisa el valor de discounted_prices para ver los precios con descuento.
discounted_prices = get_discounted_prices(prices)
# TODO 16: crea una lista de productos como tuplas (nombre, precio).
# Luego revisa el valor de products para ver la lista base.
products = [("laptop", 2500), ("mouse", 50), ("monitor", 650), ("teclado", 80)]
# TODO 17: ordena products por precio usando sorted() y key=lambda.
# Luego revisa el valor de sorted_products para ver los productos ordenados.
sorted_products = sorted(products, key=lambda x: x[1])
# TODO 18: obtiene el producto mas caro usando max() y key=lambda.
# Luego revisa el valor de most_expensive_product para ver el producto mas caro.
most_expensive_product = max(products, key=lambda x: x[1])
