# tạo ra một list chứa thứ yêu thích
# Hiện list
# cập nhật vị trí nào
# cập nhật item mới là gì
# thay thế vào
#in ra
no = 1
fav_items = ["Bun cha","Bun dau","Friends","Games"]
print("Your favorites things is :", fav_items)

# position = int(input("What do you want to replace ? ")) - 1
# new_fav = input("Replace with ? ")

# fav_items[position] = new_fav
# print(fav_items)
remove = int(input("Which one do you want to remove ? ")) - 1
for item in fav_items:

     fav_items.pop(remove)
     print(no,". ", item, sep="")

     no += 1