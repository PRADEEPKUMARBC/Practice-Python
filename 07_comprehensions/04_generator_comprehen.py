daily_sales = [5, 63, 4, 52, 7, 21, 45, 3, 20, 40]

total_cups = {sale for sale in daily_sales if sale > 5}

print(total_cups)