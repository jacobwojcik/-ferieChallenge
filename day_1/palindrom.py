print ("Type your text: ")
text = input()
pali=''
text_to_check=''
for letter in text[::-1]:
    if letter.isalpha():
        pali+=letter
for letter in text:
    if letter.isalpha():
        text_to_check+=letter
print (pali)
if text_to_check.lower() == pali.lower():
    print ("It's a palindrome!!")
else:
    print ("It's not a palindrome ;<")