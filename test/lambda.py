f = lambda x, y:x+y
print(f(2, 5))

numbers= [1,2,3,4]
squared = map(lambda x: x**2, numbers)
print(list(squared))

even = filter(lambda x:x%2==0, numbers)

print(list(even))

points = [(1,2), (3,4), (5,3), (2,4)]
sorted_points = sorted(points, key=lambda point:point[1])
print(sorted_points)