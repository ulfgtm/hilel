# persons = {'Jack':34, 'Anna':27}
# # for item in persons.items():
# #      print(item)
# persons_other = {'Anna':42, 'Jack':67,}
# persons.update(persons_other)
# print(persons)
products = [{"name": "water", "price": 12, "title": "bonaqua"},
             {"name": "bread", "price": 9, "title": "Whitebread"},
             {"name":"apple", "price": 25, "title":"Golden"}]
for product in products:
   if product["name"] == 'bread':
       # bread_prices.append(products['price'])
       product['price'] *= 2
       print(products)
