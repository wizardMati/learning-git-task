shopping = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

for shop, products in shopping.items():
    capitalized_products = [item.capitalize() for item in products]
    print(f"Idę do {shop.capitalize()}, kupuję tu następujące rzeczy: {capitalized_products}.")

total_items = sum(len(products) for products in shopping.values())
print(f"W sumie kupuję {total_items} produktówe.")


