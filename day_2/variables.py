# Day 2: 30 Days of python programming
import math

firstName = 'Michael'
lastName = 'Albert'
fullName = firstName + ' ' + lastName
country = 'United States'
city = 'Normal'
age = 31
year = 2020
is_married = False
is_true = True
is_light_on = False
fish, dog, cat = 'baal', 'Raven', 'Lily'

print(type(firstName))
print(type(lastName))
print(type(country))
print(type(age))
print(type(fish))
print('Length of first Name: ', len(firstName))
print(fullName)
print('First name: ', len(firstName), ' Last Name: ', len(lastName));


num_one = 5
num_two = 4
_total = num_one + num_two
_diff = num_one - num_two
_product = num_two * num_one
_division = num_one / num_two
_remainder = num_one % num_two
_exp = num_one ** num_two
_floor_division = num_one // num_two

print(num_one, ' + ', num_two, ' = ', _total)

area_of_circle = math.pi * 30 ** 2
circ_of_circle = 2 * math.pi * 30

print('area of circle with radius 30: ', area_of_circle)

firstName = input('Enter first name: ')
lastName = input('Enter Last Name: ')

print('Full name:', firstName, lastName)