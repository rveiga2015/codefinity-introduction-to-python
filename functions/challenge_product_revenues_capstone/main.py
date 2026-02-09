# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for index in range(len(prices)):
        revenue.append(prices[index]*quantities_sold[index])
    return revenue

teste = calculate_revenue(prices, quantities_sold)
print(teste)

"""
def formatted_output(revenues):
    sort_revenues = sorted(revenues)
    for product, revenue in sort_revenues:
        print(f"{sort_revenues[product]} has total {sort_revenues[revenue]}")

revenues = calculate_revenue(prices, quantities_sold)
print(revenues)

# revenue_per_product = list(zip(products, revenues))
# formated_output(revenue_per_product)



# Example of expected output line (do not remove):
# print(f"{revenue[0]} has total revenue of ${revenue[1]}")
"""