#first last 6
#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
def first_last6(nums):
  if nums[0] ==6 or nums[len(nums)-1]==6:
    return True
  else: 
    return False

#same first last 
#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
def same_first_last(nums):
  if len(nums)>=1 and nums[0] == nums[len(nums)-1]:
    return True
  else: 
    return False

#makepi
#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
def make_pi():
  array = [3, 1, 4]
  return array

#common end 
#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
def common_end(a, b):
    if a[0] == b[0]:
      return True 
    elif a[len(a)-1] == b[len(b)-1]:
      return True
    else:
      return False 

#sum 3
#Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
  sum = nums[0] + nums[1]+ nums[2]
  return sum

#rotate left 3
#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
def rotate_left3(nums):
  return nums[1:] + nums[:1]

#reverse 3
#Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
def reverse3(nums):
  return nums[::-1]

#max end 3
#Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
def max_end3(nums):
  a = nums[0]
  b = nums[2]
  if a>b:
    return [a,a,a]
  elif b>a:
    return [b,b,b]
  elif b==a:
    return [b,b,b]
  else:
    return nums

#sum2
#Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) <2: 
    return nums[0]
  else: 
    return nums[0] + nums[1]

#middleway
#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
def middle_way(a, b):
  a = a[1]
  b = b[1]
  array = [a, b] 
  return array

#make ends
#Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
def make_ends(nums):
  a = nums[0] 
  b = nums[len(nums)-1]
  array = [a,b]
  return array

#has 23
#Given an int array length 2, return True if it contains a 2 or a 3.
def has23(nums):
  if nums[0] == 2 or nums[1] == 2:
    return True
  elif nums[0] == 3 or nums[1]==3: 
    return True 
  else: 
    return False 

