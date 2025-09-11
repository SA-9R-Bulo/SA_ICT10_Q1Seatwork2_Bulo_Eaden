import asyncio
from js import document
from pyscript import display

# Wait for an element with a specific ID to appear in the DOM
async def wait_for_element(id):
    while not document.getElementById(id):
        await asyncio.sleep(0.05)
    return document.getElementById(id)

async def main():
    # Restaurant data
    restaurant_name = "Nihon GO!"
    owner_name = "Eaden Bulo"
    year_since = 2025
    tax_rate = 0.08
    has_delivery = True
    is_dine_in = True
    is_takeaway = False

    product_names = ["Tonkotsu Shoyu Ramen", "Pork cutlet curry", "Chicken Karaage"]
    beverages = ["Iced Tea", "Sparkling Water"]
    business_hours = ("8:00 AM", "10:00 PM")

    menu = {
        "Tonkotsu Shoyu Ramen": 370.00,
        "Chicken Karaage": 80.00,
        "Pork cutlet curry": 350.00,
        "Iced Tea": 30.00,
        "Sparkling Water": 20.00,
    }

    stock = {
        "Tonkotsu Shoyu Ramen": 11,
        "Chicken Karaage": 30,
        "Pork cutlet curry": 12,
        "Iced Tea": 25,
        "Sparkling Water": 44,
    }

    common_allergens = {"gluten", "dairy", "nuts"}


    display(restaurant_name, target="name1")
    display(f"Owner: {owner_name}", target="owner")
    display(f"Since {year_since}", target="since")
    display("Menu Pricelist", target="heading1")
    display(product_names[0], target="prod1")
    display(f"₱{menu['Tonkotsu Shoyu Ramen']:.2f}", target="price1")
    display(f"{stock['Tonkotsu Shoyu Ramen']} pcs", target="stock1")
    display(product_names[1], target="prod2")
    display(f"₱{menu['Pork cutlet curry']:.2f}", target="price2")
    display(f"{stock['Pork cutlet curry']} pcs", target="stock2")
    display(product_names[2], target="prod3")
    display(f"₱{menu['Chicken Karaage']:.2f}", target="price3")
    display(f"{stock['Chicken Karaage']} pcs", target="stock3")
    display(beverages[0], target="prod4")
    display(f"₱{menu['Iced Tea']:.2f}", target="price4")
    display(f"{stock['Iced Tea']} pcs", target="stock4")
    display(beverages[1], target="prod5")
    display(f"₱{menu['Sparkling Water']:.2f}", target="price5")
    display(f"{stock['Sparkling Water']} pcs", target="stock5")
    display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")
    display("Dine-in Available", target="orderType")

# Run it
asyncio.ensure_future(main())
