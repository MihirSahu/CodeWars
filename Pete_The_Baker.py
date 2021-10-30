#!/usr/bin/env python3

def cakes(recipe, available):

    # Find ratios of available to recipe
    recipeRatios = []
    for i in recipe.keys():
        if i in available.keys():
            recipeRatios.append(int(available[i]/recipe[i]))
        else:
            return 0

    """
    # Find lowest value in list, replaced by min()
    lowest = recipeRatios[0]
    for idx, i in enumerate(recipeRatios):
        if i < lowest:
            lowest = i
    """

    return min(recipeRatios)


# Testing
print(cakes(recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, available = {"sugar": 500, "flour": 2000, "milk": 2000}))


# Result: Success
# Optimal Solution
# def cakes(recipe, available):
#    return min(available.get(k, 0)/recipe[k] for k in recipe)
