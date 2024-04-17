#1. Write a function which generates a six digit/character random_user_id

import day_12.module as module

print(module.random_user_id())

#2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

print(module.user_id_gen_by_user(10,10))

#3.Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print(module.rgb_color_gen())


#4. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

print(module.list_of_hexa_colors(12))

#5.Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print("hello") 
print(module.list_of_rgb_colors(10))

#4.Write a function generate_colors which can generate any number of hexa or rgb colors.

#5.Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

in_list=[24,6515,235,24,654365]
print(f'i/p list {in_list}')
print(f'o/p list {module.shuffle_list(in_list)}')

#6.Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

print(module.random_orderded())

