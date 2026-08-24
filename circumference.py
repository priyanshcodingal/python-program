def circumference(radius):
    answer = 2 * 3.14 * radius
    return answer

radius = float(input("Enter the radius: "))

result = circumference(radius)

print("Circumference =", result)