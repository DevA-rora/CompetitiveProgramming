# two pointers

def two_pointers(user_list: list[int], target: int) -> bool:
    # define left & right pointers:
    left = 0
    right = len(user_list) - 1 

    # pointer movement calculations:
    while True:
        sum = user_list[left] + user_list[right]
        # if left + right pointer is the target, return true.
        if sum == target:
            return True
    
        # if the sum is greater than the target, move the right pointer down 1.
        elif sum > target:
            right -= 1

        # if the sum is less than the target, move the left pointer up
        elif sum < target:
            left += 1

        
    
user_list = [2, 4, 7, 9]
target = 9
# should yield "True"
print(two_pointers(user_list, target))

# should return an error:
user_list = [3, 6, 9, 12]
target = 300
try:
    print(two_pointers(user_list, target))
except Exception as e:
    print(f"An error occured: {e}")