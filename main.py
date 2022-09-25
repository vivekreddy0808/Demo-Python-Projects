# food_amount = input('enter your bill amount here: $')
# tip_percentage = input('enter tip amount here: $')

# tip_amount = (float(tip_percentage) / 100)
# total_bill = (int(food_amount) * float(tip_amount) + int(food_amount))

# print('$' + str(total_bill))

def bill_calculator(food, tip, tip_percentage, total):

  food = input('enter your bill amount here $: ')
  tip_percentage = input('enter tip amount here %: ')
  tip = food + (float(tip_percentage) / 100)

  total= (food + tip)
  print(float(total)


bill_calculator(100,20,0.2,120)