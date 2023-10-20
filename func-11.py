def is_palindrome(text):
 
    cleaned_text = ''.join(text.split()).lower()
    
  
    return cleaned_text == cleaned_text[::-1]


uinput = input("Enter something bro: ")

if is_palindrome(uinput):
    print(f"'{uinput}' is a palindrome.")
else:
    print(f"'{uinput}' is not a palindrome.")
