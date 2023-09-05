# Create a function that takes a name as an argument and
# returns a new string that says hello and then the name 
#that was teh argument
# Then use this function and ask the user for their name 
#and tell them hello

print("Kali")

#save a variable to the string for ease of consistency throughout document

name = "Kali"
print(name)

#To put a space between words of a string us a comma

print("Hello ", name)

#Another way to do it that allows you to store a variable is
print("Hello " + " " + name)
hello_kali = "Hello " + " " + name
print(hello_kali)

# Use "def" to create a function. Stands for definition or define
print("Our function is defined below")
def say_hello_print(the_users_name):
    print("Hello " + the_users_name)
    return None


print("using our function with the print statement inside")
say_hello_print("kali")
print(say_hello_print("kali"))

#colon lets us know that anything below the function and 4 spaces to
#The right belongs to the function
#Anything back at the far left does not below to the function   
#function lets us save code for later to reuse and not keep writing 100x
#instead of using print, we want to use a return because it is more effective in most cases

def say_hello_return(the_users_name):
    return "hello " + the_users_name

#adding "return none" renders the above function useless will return none

print("using our function with the return stsatement inside and not printing")
print(say_hello_return("steve") == "Hello Steve")

print(say_hello_return("Steve"))
hello_steve = say_hello_return("steve")
print(hello_steve)

#a function by default has a return none statement if we don't specify a return statement.
# a parameter takes the value of an argument
# an argument is the value that we give a parameter
#example of a parameter is the_users_name
#example of an argument is "steve"

users_name = input("what is your name?")
#print(users_name)
#print(type(users_name))
print(say_hello_return(users_name))



