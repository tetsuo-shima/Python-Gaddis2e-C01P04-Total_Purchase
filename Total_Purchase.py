__author__ = 'Dwight Francis'

# A customer in a store is purchasing five items. Write a program that asks for the price of each item, and then
# displays the subtotal of the sale, the amount of sales tax, and the total. Assume the sales tax is 6 percent.

SALES_TAX_RATE = 0.06
subtotal = 0.0

def calc_sales_tax(subtotal):
    return subtotal * SALES_TAX_RATE

def calc_total(subtotal):
    return subtotal + calc_sales_tax(subtotal)

def display_cash(money):
    return format(money, ',.2f')

for item_number in range(1,6):
    subtotal += (float(input('Enter price for item %d: $' %item_number)))

print('\nTotal: $', display_cash(subtotal), sep='')
print('Tax: $', display_cash(calc_sales_tax(subtotal)), sep='')
print('Total: $', display_cash(calc_total(subtotal)), sep='')




