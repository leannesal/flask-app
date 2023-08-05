import string

password='njknon'
print(string.punctuation)
if not any(char in string.punctuation for char in password):
    print('yes')


