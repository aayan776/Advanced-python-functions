data = {"set1" : {1,2,3,4,6}, "set2" : {1,2,3,7,5}, "set3" : {1,2,9,4,5}}
result = set.intersection(*data.values())
print(f"Intersection of all values: {result}")
#List comprehension
numbers = [1,4,5,7,2,8,10,12,24,72]
list1 = [x for x in numbers if x % 2 == 0]
print(f"All even numbers: {list1}")
#Dictionary comprehension
squares = {str(x) : x ** 2 for x in [1,5,10,15,20,25]}
print(squares)
#Map funcntion
def cubes(n):
    return n ** 3
num = [1,5,10,15,20,25]
result = map(cubes, num)
print(list(result))
#zip function
names = ["Tawseef", "Mamun", "Aayan", "Anaya", "Ashrafi"]
age = [14, 14, 14, 1, 23]
zipped = zip(names, age)
print(list(zipped))
#lambda
num1 = [1,2,3,4,5]
num2 = [6,7,8,9,10]
result = map(lambda x, y : x + y, num1, num2)
print(list(result))
#zip in reverse
list2 = [10,20,30,40,50]
list3 = [100,200,300,400,500]
for x, y in zip(list2 , list3[::-1]):
    print(x, y)
#zipping dictionary
stocks = ["Stock1", "Stock2", "Stock3"]
prices = [1200, 2175, 2345]
dict1 = {stocks : prices for stocks, prices in zip(stocks, prices)}
print(format(dict1))
#Exit
if age[0] < 18:
    print("Age not allowed. Exiting...")
    exit()
elif age[0] > 18:
    print("Age eligible")