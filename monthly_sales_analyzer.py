# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
        
    total = 0
    for day_sale in data:
        total += day_sale.get(product_key, 0)
    return total

ventas_a = total_sales_by_product(sales_data, "product_a")
print("ventas totales A", ventas_a)
ventas_b = total_sales_by_product(sales_data, "product_b")
print("ventas totales B", ventas_b)
ventas_c = total_sales_by_product(sales_data, "product_c")
print("ventas totales C", ventas_c)
ventas_totales = ventas_a + ventas_b + ventas_c
print("ventas totales", ventas_totales)

total_sales_by_product

def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
          
    total = 0
    for day_sale in data:
        total += day_sale.get(product_key, 0)
    return total

cantidad_de_dias = len(sales_data)

ventas_a = (round(total_sales_by_product(sales_data, "product_a")/cantidad_de_dias))
print("promedio de ventas diarias A", ventas_a)
ventas_b = (round(total_sales_by_product(sales_data, "product_b")/cantidad_de_dias))
print("promedio de ventas diarias B", ventas_b)
ventas_c = (round(total_sales_by_product(sales_data, "product_c")/cantidad_de_dias))
print("promedio de ventas diarias C", ventas_c)
ventas_totales = round((ventas_a + ventas_b + ventas_c)/3)
print("promedio de ventas diarias totales", ventas_totales)

average_daily_sales

def best_selling_day(data):
    """Finds the day with the highest total sales."""
    max_sales_day = 0
    best_day = 0

    for day_data in data:
        total = day_data["product_a"]+day_data["product_b"]+day_data["product_c"]

        if total > max_sales_day:
            max_sales_day = total
            best_day = day_data["day"]

    return best_day, max_sales_day

day, total = best_selling_day(sales_data)
print(f"el dia con mayor ventas es el {day} ,con un total de {total}")

 
def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    
    count = 0

    for day_sale in data:
        sales = day_sale.get(product_key, 0)

        if sales > threshold:
            count +=1
    
    return count

resultado = days_above_threshold(sales_data, "product_c", 300)
print(f"Dias cuando C excede 300 en ventas {resultado} dias")
    
     
def top_product(data):
    """Determines which product had the highest total sales in 30 days."""

    total_ventas = {
        "product_a": 0,
        "product_b": 0,
        "product_c": 0
    }

    for dia in data:
        total_ventas["product_a"] += dia["product_a"]
        total_ventas["product_b"] += dia["product_b"]
        total_ventas["product_c"] += dia["product_c"]

        top_ABC = max(total_ventas, key=total_ventas.get)
        Ventas_totales_ABC = total_ventas[top_ABC]
    
    return top_ABC, Ventas_totales_ABC

nombre, cantidad = top_product(sales_data)

print(f"El mas vendido es {nombre} con {cantidad} und.")

        

# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
