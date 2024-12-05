def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total
