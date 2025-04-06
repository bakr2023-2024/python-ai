eggs=19.11
beans=20.44
ketchup=1.33
budget=50.55
total_items=eggs+beans+ketchup
diff=budget-total_items
if diff < 0:
    print(f'insufficient funds. ${-diff:.2f} is required')
elif diff > 0:
    print(f'purchase successful. ${diff:.2f} remained')
else:
    print(f'purchase successful. no remainder')