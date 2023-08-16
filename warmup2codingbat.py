#string times
#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
  return str * n

#front times
#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
def front_times(str, n):
  return str[:3]*n

#string bits 
#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
  string = ""
  for i in range(len(str)):
    if i%2==0:
      string = string + str[i]
  return string

#string splosion
#Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
  string = ""
  for i in range(len(str)):
    string = string + str[:i+1]
  return string

#last 2
#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
  if len(str) < 2:
    return 0
  count = 0
  end = str[len(str)-2:]
  for i in range(len(str)-2):
   if str[i:i+2] == end:
     count = count+1
  return count

#array count 9
#Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
  count = 0 
  for i in nums: 
    if i == 9:
      count +=1
  return count

#arrat front 9
#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
def array_front9(nums):
  #true if 1 of first 4 is 9
  end = len(nums)
  if end>4:
    end = 4
  
  for i in range(end):
    if nums[i] == 9:
      return True
  return False

#array123
#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

#string match
#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count
