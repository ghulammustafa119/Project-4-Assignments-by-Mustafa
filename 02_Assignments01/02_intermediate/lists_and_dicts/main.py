# Problem #1: List Practice
def main():
    fruit_list:list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
     
    print(f"fruit_list {fruit_list}")
    
    # Print the length of the list.
    print(f"Length {len(fruit_list)}")
    
    # Add 'mango' at the end of the list. 
    fruit_list.append("mango")
    
    # Print the updated list.
    print(f"Print the updated list {fruit_list}")
    
main()


# Problem #2: Index Game
def acces_element(lst:list,index:int):
    if 0 <= index < len(lst):
        return lst[index]
    else: 
        return "Index out of range!"
    
def modify_element(lst:list,index,new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return "Element updated successfully!"
    else:
        return "Index out of range!"
    
def slice_list(lst:list,start,end):
    if 0 <= start < len(lst) and 0 <= end < len(lst) and start < end:
        return lst[start:end]
    else:
        return "Invalid slice range!"
    
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
while True:
    print("-"*20)
    print("Choose an operation: check list / access / modify / slice / pop / exit")
    choice = input("Enter Your Choice ")

    if choice == "access":
        index = int(input("Enter Index: "))
        print( acces_element(my_list,index) )

    elif choice == "modify":
        index = int(input("Enter Index: "))
        new_value_raw = input("Enter new Value: ")

        # Convert to number if possible
        if new_value_raw.isdigit():
            new_value = int(new_value_raw)
        else:
            try:
                new_value = float(new_value_raw)
            except ValueError:
                new_value = new_value_raw.lower()

        print(modify_element(my_list, index, new_value))
        print("Updated List:", my_list)

    elif choice == "slice":
        start = int(input("start Num : "))
        end = int(input("end Num : "))
        print( slice_list(my_list,start,end) )

    elif choice == "check list":
        print(f"My List: {my_list}")

    elif choice == "pop":
        my_list.pop()

    elif choice == "exit":
        break
