def linear_search_product(products, target_product):
  indices = []
  for index, product in enumerate(products):
      if product == target_product:
          indices.append(index)
  return indices

# Example usage:
products_list = ["Apple", "Orange", "Banana", "Orange", "Grapes", "Orange"]
target = "Orange"

result = linear_search_product(products_list, target)

if result:
  print(f"The product '{target}' found at indices: {result}")
else:
  print(f"The product '{target}' not found.")
