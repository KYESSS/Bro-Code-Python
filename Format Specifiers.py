# format specifiers = {:flags} format a value based on what
#                              flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plug sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :. = comma separator

price1 = 4561.123
price2 = -100.05
price3 = 78492.2345

print(f"Price 1 is £{price1:+,.2F}")
print(f"Price 2 is £{price2:+,.2F}")
print(f"Price 3 is £{price3:+,.2F}")