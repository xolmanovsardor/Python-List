nums = []
while True:
    choice = input("dllfirflirjfi")
    if choice == "ha":
        element = int(input())
        nums.append(element)
    else:
        break

uneque_nums = []
for num in nums:
    if nums.count(num) != 1 and num not in uneque_nums:
        uneque_nums.append(num)
        

print(uneque_nums)

