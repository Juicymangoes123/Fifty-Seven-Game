import random
set_a = [1,2,3,4,5,6,7,8,9]
#print(num)
#print(num_2)
sum = 0
#set_b = set()
#allowable_set_one
#one = [2,3,4,7]
#allowable_set_two
#two = [1,3,5,8]
#allowable_set_three
#three = [1,2,6,9]
#allowable_set_four
#four = [1,5,6,7]
#allowable_set_five
#five = [2,4,6,8]
#allowable_set_six
#six = [3,4,5,9]
#allowable_set_seven
#seven = [1,4,8,9]
#allowable_set_eight
#eight = [2,5,7,9]
#allowable_set_nine
#nine = [3,6,7,8]


def allowable_set(num):
        if num == 1:
            allowable = [2,3,4,7]
        if num == 2:
            allowable = [1,3,5,8]
        if num == 3:
            allowable = [1,2,6,9]
        if num == 4:
            allowable = [1,5,6,7]
        if num == 5:
            allowable = [2,4,6,8]
        if num == 6:
            allowable = [3,4,5,9]
        if num == 7:
            allowable = [1,4,8,9]
        if num == 8:
            allowable = [2,5,7,9]
        if num == 9:
            allowable = [3,6,7,8]
        num_3 = random.choice(allowable)
        return num_3

while sum < 57:
    num = random.choice(set_a)
    num_3 = allowable_set(num)
   # if num == num_3:
   #     num_3 = random.choice(set_a)
    print("Number One:", num)
    sum += num
    print("Sum:", sum)
    if sum < 57:
        print("Number Two:", num_3)
        sum += num_3
        print("Sum:", sum)
    #set_b.add(num)
    #set_b.add(num_2)
    #for x in set_b:
    #    sum += x
    #set_b.pop()
    #set_b.pop()
print("End of while loop")
