#count evens 
#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
def count_evens(nums):
  counter = 0
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      counter += 1
  return counter 

#big diff
#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
def big_diff(nums):
  return max(nums) - min(nums)

#centered average 
#Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
def centered_average(nums):
    sum = 0
    total = len(nums)-2
    largest = nums.index(max(nums))     
    smallest = nums.index(min(nums))    
    if largest == smallest:             
        for i in range(len(nums)):      
            if nums[i] == nums[smallest]:
                largest = i             
    for i in range(len(nums)):
        if i != largest and i != smallest:      
            sum = sum + nums[i] 
    if total > 0:
        return sum / total         
    else:
        return sum  

#sum 13 
#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
def sum13(nums):
  #sum of numbers in an array 
  #0 for empty array
  #any numbers after 13 and 13 do not count in the array 
  sum = 0 
  for i in range(len(nums)):
    if nums[i] != 13:
      sum +=nums[i]
    elif nums[i] == 13 and i <len(nums)-1:
      nums[i] =0
      nums[i+1] = 0
  return sum

#sums 67
#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
#check if the number is a 6 
#if the number is a 6 -> i will count the numbers as 0 until i get to the 7 
#then i will move on and count the numbers as i go on
#sum of the numbers in the array
#IGNORE when the number is 6->7    
def sum67(nums):
  sum = 0 
  i=0
  while i < len(nums):
    if nums[i] == 6: 
      while nums[i] != 7: 
        i+=1
      i+=1
    elif i <len(nums) and nums[i] != 6:
      sum += nums[i] 
      i+=1 
  return sum
        
# has 22
# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(nums):
  #loop through the array 
  #check if theres a 2 -> next # is a 2
  #return True 
  #if no return False
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True 
  return False

