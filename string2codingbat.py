#double char 
#Given a string, return a string where for every char in the original, there are two chars.
def double_char(str):
  result = ""
  for i in range(len(str)):
    result = result + str[i]
    result = result + str[i]
  return result

#count hi
#Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
  counter = 0
  for i in range (len(str)-1): #its -1 because you are adding i+1 in the following line, meaning this would get to the last letter in the string and have no where else to go
        if str[i] == 'h' and str[i+1] == 'i':
            counter+=1
  return counter

#cat dog 
#Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
    counter1 = str.count("cat")
    counter2 = str.count("dog")
    
    
    if(counter1 == counter2):
       return True
    else:
       return False

#count code
#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
  counter = 0 
  for i in range(len(str)-3):
    if str[i]=="c" and str[i+1]=="o" and str[i+3]=="e":
      counter+=1
  return counter

#end other 
#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
def end_other(a, b):
  a1 = a.lower()
  b1 = b.lower()
  if a1.endswith(b1) or b1.endswith(a1):
    return True 
  else: 
    return False

#xyz there
#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
def xyz_there(str):
  return str.count(".xyz") != str.count("xyz")


