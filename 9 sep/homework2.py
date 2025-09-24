  #1
n = int(input("enter the no. of piles :"))
if n % 2 == 0:
    step = 2
else:
    step = 2
for i in range(n):
    print(n+i*step)

# 2 wap to find a list of integer containing exactly five distinct value;such that no integer repeats consecutively.

my_list = ['1', '2' ,'1' ,'1', '3', '4', '4','5','2','3', '2','1','5']
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
if len(new_list) ==5:
    print("yes")
else:
    print("no")

#3 wap a python to print the indexes of no. in a given list that are below a give threshold value.
my_list = [ 10, 20, 30, 40, 50, 60, 70, 80, 90]
threshold = 50
indexes = []
for i  in range(len(my_list)):
    if my_list[i] < threshold:
        indexes. append(i)
print(indexes)
#5 wap to find the lenght of the a given list of nonempty list.
lists = ["cat","dog", "tiger","elephant"]
for i in lists:
    print(len(i))
#4 wap to check whethera given strings are palindromes or not . return true otherwise false.

s = "mom"
a = s[ : : -1] 
print(s[ : : -1])
if s == a :
    print("yes")
else:
    print("no")

list = ["racecar", "radhekrishna", "sitaram","mam", "mom"]
for i in list: 
   a = i[ : : -1]
   if i == a :
       print(i + "is palindrome")
   else:
       print(i + "is not palindrome")

# copy a paragraph from today's news as a string (str = "<paragraph>")where you substitute<> with the actual news paragraph. print total number of letters, 
# words and lines in the news paragraph . in the form of : 115 45 7
str = """the global economy is facing significant challengers due to a combination of factors including inflation, supply chain disruptions, and geopolitical tensions.
      central banks around the world are grappling with the task of curbing inflation while supporting economic growth."""
# count letters (only alphabets, not spacing)
letters = sum(c.isalpha() for c in str)

# count words
words = len(str.split())

# count lines
lines = str.count("\n") +1  # each newline means 1 extra line
print(letters , words, lines)

#1
s = [1, 4,3,4,3,2,4,3,2,1,5,1,3,5,6,4,6,3,2,1,4,3]
p = []
for i in s:
    if i not in p:
        p.append(i)
print(p)


#2

s = [1,2,3,4,5,2,3,1,4,3,2,3,3,2,4,1,2 ]
d ={}
for i in s :
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

#3
a = [23,45,56,12,34]
i = a[0]
for x in a[1:]:
    if x >i:
        i = x
print(i)

#4
with open("demo.txt", "r") as file:
    for line in file:
        if "hello" in line.lower():
            print(line.strip())
    

#5 given a list of words, group them dictionarywhere
#  the key is first letter and the value is a list of words starting with that letter.

words = ["apple", "banana","apricot","bluberry", "cherry", "cat"]
group = {}

for i in words:
    group.setdefault(i[0].lower(),[]).append(i)
print(group)




