#create squares of numbers from 1 to 10 in a list using list comprehension
#squares= [x*x for x in range(1,11)]
#print(squares)

#s=input("Enter a string: ")
#list1=[x for x in s]
#print(list1)

#numbers=[1,2,3,4,5]
#cubedict={x:x*x*x for x in numbers}
#print(cubedict)

#sentence="the quick brown fox jumps over the lazy dog"
#unique={x for x in sentence if x in ['a', 'e', 'i', 'o', 'u']}
#print(unique)

#find all numbers from 1 to 100 that are divisible by 3 and 5 using list comprehension
# divisible_by_3_and_5 = [x for x in range(1,101) if x%15==0]
# print(divisible_by_3_and_5)

#list comprehension odd numbers remain same and even numbers are replaced by even  
# list1=['even' if x%2==0 else x for x in range(1,11)]
# print(list1)

#word and corresponding length in a dictionary using dict comprehension
#sentence="the quick brown fox jumps over the lazy dog"
#words=sentence.split()
#wordandlength={x:len(x) for x in words}
#print(wordandlength)

#find unique elements from a list without using set() function
#l1=[1,2,3,4,5,1,2,3]
#l2=[]
#[l2.append(i) for i in l1 if i not in l2 ]
#print(l2)

#convert nested list to single list using list comprehension
#nested_list=[[1,2,3],[4,5],[6,7,8]]
#flat_list=[j for i in nested_list for j in i]
#print(flat_list)

#list of strings and filter out ones that have fewer than length 5 using lambda or do not start with an uppercase

# words=['Apple','Banana','cherry','dog','elephant','fig']
# filtered_words=list(filter(lambda x: len(x)>=5 and x[0].isupper(), words))
# print(filtered_words)

#find the product of all numbers in a list using lambda 
#from functools import reduce
#list1=[2,-3,4,-1,5,0]
#positive=list(filter(lambda x : x>0, list1))
#product=reduce(lambda x,y:y*x, positive)
#print(product)