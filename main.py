from pyscript import display
# Restaurant Order System using Python Data Types

# String data type
restaurant_name = "Nihon GO!"
owner_name = "Eaden Bulo"

# Integer data type
year_since = 2025

# Float data type
tax_rate = 0.08  # 8% tax

# Boolean data type
has_delivery = True
is_dine_in = True
is_takeaway = False

# List data type
product_names = ["Tonkotsu Shoyu Ramen", "Pork cutlet curry", "Chicken Karaage"]
beverages = ["Iced Tea", "Sparkling Water"]

# Tuple data type
business_hours = ("8:00 AM", "10:00 PM")

# Dictionary data type
menu = {
    "Tonkotsu Shoyu Ramen": 370.00,
    "Chicken Karaage": 450.00,
    "Pork cutlet curry": 450.00,
    "Iced Tea": 30.00,
    "Sparkling Water": 20.00,
}

stock = {
    "Tonkotsu Shoyu Ramen": 11,
    "Chicken Karaage": 10,
    "Pork cutlet curry": 12,
    "Iced Tea": 15,
    "Sparkling Water": 14,
}

# Set data type
common_allergens = {"gluten", "dairy", "nuts"}

# Displaying restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")
stocks = [15, 10, 20, 30, 20]
# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Tonkotsu Shoyu Ramen']:.2f}", target="price1")
display(f"{stocks[0]} pcs", target="stock1")
display(product_names[1], target="prod2")
display(f"₱{menu['Pork cutlet curry']:.2f}", target="price2")
display(f"{stocks[1]} pcs", target="stock2")
display(product_names[2], target="prod3")
display(f"₱{menu['Chicken Karaage']:.2f}", target="price3")
display(f"{stocks[2]} pcs", target="stock3")
display(beverages[0], target="prod4")
display(f"₱{menu['Iced Tea']:.2f}", target="price4")
display(f"{stocks[3]} pcs", target="stock4")
display(beverages[1], target="prod5")
display(f"₱{menu['Sparkling Water']:.2f}", target="price5")
display(f"{stocks[4]} pcs", target="stock5")



# Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")


# Display order type
display(f"Dine-in Available", target="orderType")