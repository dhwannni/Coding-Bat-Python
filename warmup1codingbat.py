#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#sleep_in
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
#monkey trouble 
def monkey_trouble(a_smile, b_smile):
  #both smiling- true 
  #neither smiling- true 
  if a_smile and b_smile: 
    return True
  if not a_smile and not b_smile:
    return True 
  else: 
    return False

#Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#sum double 
def sum_double(a, b):
  if a==b: 
    return (a+b)*2
  else: 
    return (a+b)

#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
#diff21
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2

#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
#parrot trouble
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

#Giiven 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
#makes10
def makes10(a, b):
  if a==10 or b==10: 
    return True 
  if a+b==10:
    return True 
  else: 
    return False
  
#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
#near hundred 
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

#Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
#pos neg
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
  
#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
#not string
def not_string(str):
  if len(str)>=3 and str[:3] =="not":
    return str
  else: 
    return "not " + str
  
#Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
#missing char
def missing_char(str, n):
 front = str[:n]   # up to but not including n
 back = str[n+1:]  # n+1 through end of string
 return front + back

#Given a string, return a new string where the first and last chars have been exchanged.
#front back
def front_back(str):
  if len(str) <=1: 
    return str
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]

#Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
#front 3
def front3(str):
  # Figure the end of the front
  if len(str) <=3:
    return str + str + str
  else:
    front= str[:3]
    return front + front + front