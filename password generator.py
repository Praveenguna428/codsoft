
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) 
    for i in range(length))
    return password

def main():
    try:
        print("   =============================================================   ")
        print("   ================== PYTHON PASSWORD GENERATOR ================    ")
        print("   =============================================================   ")
    
        
        length = int(input("   Enter the desired length of the password : "))
        
        
        print("   -------------------------------------------------------------    ")
        if length < 8 or length > 128:
            print("Password length must be between 8 and 128 characters.")
        else:
            complexity = input("   Choose password complexity (weak/medium/strong): ")
            print("   -------------------------------------------------------------    ")

            complexity=complexity.lower()
            if complexity == "weak":
                characters = string.ascii_letters
            elif complexity == "medium":
                characters = string.ascii_letters + string.digits
            elif complexity == "strong":
                characters = string.ascii_letters + string.digits + string.punctuation
            else:
                print("Invalid complexity level. Using strong complexity by default.")
                characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(length))
            print("                Generated Password:", password)
            print("   _____________________________________________________________   ")
            print("   ============= YOUR PASSWORD GENERATED SUCCESSFULLY ==========    ")
            print("   _____________________________________________________________   ")
            
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
