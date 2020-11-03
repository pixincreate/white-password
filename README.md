# White-Password  
A simple approach to Secure Password Input in python.  

## Why white-password?  
No-human in this world wish to get their Passwords to get leaked out.
Python script that you write will **not** know that you're entering a **password** until and unless you use **_[white-password](https://github.com/pixincreate/white-password/blob/main/white-password.py)_** which hides
the user input in a much more secure way.
No-one will ever know how long your password is either as you see an empty line with a blank space.  

## Usage:  
Copy and paste the entire method / function in your code.
Equate and Call the function with a subscript.

#### Example of usage:  
```
def white_password(prompt):      # Check src(white-password.py)
    ...
    ...
    return ...

USERNAME = input("User Name : ")      # A simple user input
PASSWORD = white_password(prompt="Password  : ")      # Calling the white_password(). You can write what ever you wish inside the double quotes.
```

