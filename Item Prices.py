price_1 = input('Please enter the cost of the first item: ') + 'p'
price_2 = input('Please enter the cost of the second item: ') + 'p'
price_3 = input('Please enter the cost of the third item: ') + 'p'
price_4 = input('Please enter the cost of the fourth item: ') + 'p'
price_5 = input('Please enter the cost of the fifth item: ') + 'p'

print(price_5)

price_list = (price_1[-1], price_2[-1], price_3[-1], price_4[-1], price_5[-1])

print("Total price is:", str(sum(price_list))+'p')
print("Average price is:", str(sum(price_list)/ (5))+'p')
print("Highest price is:", str(max(price_list))+'p')
print("Lowest price is:", str(min(price_list))+'p')