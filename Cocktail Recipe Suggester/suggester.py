import numpy as np
import pandas as pd
import random

def prettyPrint(list):
    print("Ingredients:")
    for i in list:
        if i[0] == ".":
            print("- 0" + i)
        else:
            print("- " + i)

# Data handling
df = pd.read_csv('dataset/hotaling_cocktails - Cocktails.csv')
increment = 0
unique_ingredients = set()

for index, cellvalue in enumerate(df.iloc[:, 4]):
    # Split the cell value by commas
    ingredients = cellvalue.split(',')
    
    for ingredient in ingredients:
        
        ingredient = ingredient.strip()
        unique_ingredients.add(ingredient)
        
# Convert the set to a list for sampling
unique_ingredients_list = list(unique_ingredients)

# Randomly sample 5 ingredients from the list
random_ingredients = random.sample(unique_ingredients_list, min(5, len(unique_ingredients_list)))
prettyPrint(random_ingredients)

