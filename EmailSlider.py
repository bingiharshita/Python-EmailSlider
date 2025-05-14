email=input("Enter your email address: ")
username=email[:email.index('@')]
domain=email[email.index('@')+1:]
print(f"The username is {username} and the domain is {domain}")
