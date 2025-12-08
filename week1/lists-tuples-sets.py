#Create a list of 5 user names
#Convert to a tuple & set
#Print all three
user_list = ["Ashenafi", "Victor", "john", "Mike", "Anna"]
user_tuple = tuple(user_list)
user_set = set(user_list)
print(user_list, user_tuple,  user_set)
##['Ashenafi', 'Victor', 'john', 'Mike', 'Anna'] 
# ('Ashenafi', 'Victor', 'john', 'Mike', 'Anna') 
# {'Mike', 'Victor', 'Ashenafi', 'john', 'Anna'}

sentence = input("Enter you sentence")
print("your sentence is: " + sentence)
word1 = input('Enter the word to replace: ')
word2 = input('Enter the word to repce it with: ')
print(sentence.replace(word1, word2)) 