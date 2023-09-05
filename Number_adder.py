#Create a function what will add up all the numbers in a 
#list of numbers that was given as an argument
#use this function to ask the user for a series of numbers
#and then show the user the sum of all the numbers
#that were given by the user

#each number in the list has an index number starting at 0
 #          0 1 2 3 4

my_nums = [2,4,6,8,10]

print(my_nums)
print(my_nums[0])
print(my_nums[4])
print(type(my_nums))
print(type(my_nums[0]))

my_total = 0
my_total = my_total + my_nums[0]
my_total = my_total + my_nums[1]
my_total = my_total + my_nums[2]
my_total = my_total + my_nums[3]
my_total = my_total + my_nums[4]
print(my_total)

#another way to get the total sum of numbers below
print(sum(my_nums))

#the most efective way to do this is with a "for loop"

new_total = 0
for num in my_nums:
    new_total = new_total + num
print(new_total)

#paramater is "my_list"
#argument my list numbers
def total_my_list(my_list):
    total = 0
    for num in my_list:
        total = total + num
    return total

print(total_my_list(my_nums))
print(total_my_list([2,4,6,8,10]))
print("="*25)

#while loop
x = 7
while x != "quit":
    print("the value of x is", x)
    x = x + 1
    if x == 10:
        x = "quit"

user_num = input("Tell me a number?")
print(user_num)
print(type(user_num))

#convert string to integer
user_num = int(user_num)
print(type(user_num))

#how to append
my_test_list = [100,101,102,103]
print(my_test_list)
my_test_list.append(104)
print(my_test_list)

a_number = input("Give me a number to add to your total or type 'quit' to quit ")
#if double quotes outside must use single quote inside. single quote outside, must use double quote inside.

num_list = []
while a_number != "quit":
    num_list.append(int(a_number))
    a_number = input("Give me a number to add to your total or type 'quit' to quit ")

print("The total of your list is", total_my_list(num_list))





