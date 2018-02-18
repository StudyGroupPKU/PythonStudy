from ch05_1_classes import *

apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_fruit_layer = AddLayer()
mul_tax_layer = MulLayer()

apple_price = mul_apple_layer.forward(apple, apple_num)
orange_price = mul_orange_layer.forward(orange, orange_num)
fruit_price = add_fruit_layer.forward(apple_price, orange_price)
total_price = mul_tax_layer.forward(fruit_price, tax)
print(apple_price, orange_price, fruit_price, total_price)

dtotal_price = 1
dfruit_price, dtax_price = mul_tax_layer.backward(dtotal_price)
dapple_price, dorange_price = add_fruit_layer.backward(dfruit_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)
print(dtax_price, dapple, dapple_num, dorange, dorange_num)

