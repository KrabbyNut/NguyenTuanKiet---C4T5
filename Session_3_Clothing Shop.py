# Em ko tìm được cách nào để làm cho mình gõ thường và hoa
#  mà nó vẫn hoạt động được, em chỉ làm được một trong hai

# C = ['C', 'c']
# R = ['R', 'r']
# U = ['U', 'u']
# D = ['D', 'd']
options = ['C', 'R', 'U', 'D']
s = "Our items: "
list_of_clothings = ['T-shirt', 'Sweater', 'Hoodie', 'Flannel']
orders = input("Welcome to our shop, what do you want (C,R,U,D) ? ")


if orders == options[0]:
    new_item = input("Enter new items: ")
    list_of_clothings.append(new_item)
    print(s, list_of_clothings)

if orders == options[1] :
    print(list_of_clothings)

if orders == options[2]:
    print(list_of_clothings)

    update_pos = int(input("Item update position: "))
    update_items = input("New item ? ")
    list_of_clothings[update_pos - 1] = update_items
    print(s, list_of_clothings)

elif orders == options[3]:
    print(list_of_clothings)

    delete_pos = int(input("Which item do you want to remove ? "))
    del list_of_clothings[delete_pos]
    print(s, list_of_clothings)

else:
    print("If you dont need anything then get the fuck out !!")