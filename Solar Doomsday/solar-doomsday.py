'''
    Write a function func(area) that takes as its input a single unit of measure
    representing the total area of solar panels you have (between 1 and 1000000 inclusive) and
    returns a list of the areas of the largest squares you could make out of those panels,
    starting with the largest squares first.
    So, following the example above, func(12) would return [9, 1, 1, 1]
'''
def create_solar_panels(area):
    list_of_largest_squares = []

    # Validation of given area
    if area < 1:
        return "Total area must be between 1 and 1000000"

    if area > 1000000:
        return "Total area must be between 1 and 1000000"

    if area == 1:
        return area

    while area > 0:
        biggest_square = int(area ** 0.5)
        biggest_square_area = biggest_square ** 2
        area = area - biggest_square_area
        list_of_largest_squares.append(biggest_square_area)

    return list_of_largest_squares


print(create_solar_panels(12))
print(create_solar_panels(1))
print(create_solar_panels(0))
print(create_solar_panels(1000001))
