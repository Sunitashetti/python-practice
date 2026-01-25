# Python Lists - Basic Practice

nums = [10, 20, 30, 40, 50]

# Indexing
print(nums[0])
print(nums[-1])

# Slicing
print(nums[1:4])

# Operations
nums.append(60)
nums.insert(2, 25)
nums.remove(40)
nums.pop()

# Built-in functions
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))

# Sorting and reversing
nums.sort()
nums.reverse()

print("Final List:", nums)
