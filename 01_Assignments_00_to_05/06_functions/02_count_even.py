# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!





def count_even(lst):
    
    count = 0  
    for num in lst:  
        if num % 2 == 0:  
            count += 1  
    print(count)  

def get_list_of_ints():
   
    lst = [] 
    user_input = input("Enter an integer or press enter to stop: ") 
    while user_input != "":  
        lst.append(int(user_input))  
        user_input = input("Enter an integer or press enter to stop: ")  
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()