import csv

expenses = [
    {'item_name': 'Pink Lady Apples (1.5kg)','amount': '49.99', 'category': 'Fruit', 'description': 'Bag of crisp, sweet red apples.'},
    {'item_name': 'Rotisserie Chicken','amount': '119.99', 'category': 'Meat', 'description': 'Hot, roasted whole chicken with herb seasoning.'},
    {'item_name': 'Chuckles (125g)','amount': '64.99', 'category': 'Sweets', 'description': 'Malted puffs covered in milk chocolate.'},
    {'item_name': 'Ayrshire Milk (2L)','amount': '45.99', 'category': 'Dairy', 'description': 'Fresh full-cream milk in a plastic jug.'},
    {'item_name': 'Plain T-Shirt','amount': '159.00', 'category': 'Clothes', 'description': 'White cotton crew-neck shirt.'},
    {'item_name': 'Beef Lasagna (1kg)','amount': '179.99', 'category': 'Dinner', 'description': 'Ready-made pasta meal with mince and white sauce.'},
    {'item_name': 'Sparkling Water (500ml)','amount': '16.99', 'category': 'Drink', 'description': 'Lemon-flavoured fizzy water, sugar-free.'},
    {'item_name': 'Hass Avocados (4 pk)','amount': '69.99', 'category': 'Fruit', 'description': 'Net bag of four ripe avocados.'},
    {'item_name': 'Chicken Mayo Sandwich','amount': '54.99', 'category': 'Lunch', 'description': 'Triangular bread wedges with chicken filling.'},
    {'item_name': 'Wine Gums (400g)','amount': '42.99', 'category': 'Sweets', 'description': 'Chewy fruit-flavoured gum sweets.'},
    {'item_name': 'Reusable Shopper','amount': '12.00', 'category': 'Bag', 'description': 'Black fabric bag made from recycled plastic.'},
    {'item_name': 'Double Cream Yoghurt (1kg)','amount': '47.99', 'category': 'Dairy', 'description': 'Thick plain yoghurt in a tub.'},
    {'item_name': 'Sliced White Bread','amount': '18.99', 'category': 'Bakery', 'description': 'Soft loaf of white bread, pre-sliced.'},
    {'item_name': 'Free Range Eggs (18 pk)','amount': '109.99', 'category': 'Eggs', 'description': 'Large box of mixed-size free-range eggs.'},
    {'item_name': 'Salt & Pepper Chips (150g)','amount': '24.99', 'category': 'Chips', 'description': 'Crinkle-cut potato chips with black pepper seasoning.'},
    {'item_name': '100% Orange Juice (1.5L)','amount': '39.99', 'category': 'Drink', 'description': 'Pulp-free fruit juice in a plastic bottle.'},
    {'item_name': 'Greek Salad','amount': '64.99', 'category': 'Salad', 'description': 'Bowl of lettuce, tomatoes, cucumber, olives, and feta.'},
    {'item_name': 'Rump Steak (2 pk)','amount': '189.99', 'category': 'Meat', 'description': 'Two thick cuts of matured beef steak.'},
    {'item_name': 'Ankle Socks (5 pk)','amount': '129.00', 'category': 'Clothes', 'description': 'Pack of five black cotton socks.'},
    {'item_name': 'Hand Wash (500ml)','amount': '39.99', 'category': 'Toiletries', 'description': 'Liquid soap with a lavender scent.'}
]

filename = 'expenses.csv'
with open(filename, mode='w', newline='') as file:
    fieldnames = ['item_name', 'amount', 'category', 'description']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(expenses)

print(f"File '{filename}' has been created successfully!")