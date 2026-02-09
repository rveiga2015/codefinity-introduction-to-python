def apply_discount(price, discount = .05):
    discounted_price = price * (1 - discount)
    return discounted_price

def apply_tax(price, tax = .07):
    taxed_price = price * (1 + tax)
    return taxed_price

def calculate_total(price, discount = .05, tax = .07):
    total_price = apply_discount(apply_tax(price, tax), discount)
    return total_price

total_price_default = calculate_total(120)
total_price_custom = calculate_total(100, discount = .1, tax = .08)

print(f'Total cost with default discount and tax: ${total_price_default}')
print(f'Total cost with custom discount and tax: ${total_price_custom}')





