import string
import secrets

def get_valid_password_length() -> int:
    """
    Handles user input and ensures the password length is structurally sound.
    Returns an integer representing a secure password length.
    """
    while True:
        try:
            user_input = input("Enter desired password length (minimum 8 characters): ").strip()
            length = int(user_input)
            
            if length < 8:
                print("❌ Security Warning: Passwords shorter than 8 characters are easily cracked. Please choose 8 or more.")
                continue
                
            return length
        except ValueError:
            print("❌ Invalid Input: Please enter a valid whole number.")

def generate_secure_password(length: int) -> str:
    """
    Generates a cryptographically secure, unpredictable random password.
    Guarantees at least one character from each essential group.
    """
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "@#$!%*?&"  
    
    
    all_characters = lowercase + uppercase + digits + special_chars
    
    
    password_template = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special_chars)
    ]
    
    
    remaining_length = length - len(password_template)
    password_template += [secrets.choice(all_characters) for _ in range(remaining_length)]
    
   
    secrets.SystemRandom().shuffle(password_template)
    
   
    return "".join(password_template)

def main():
    print("=" * 50)
    print("🔒 PASSWORD GENERATOR 🔒")
    print("=" * 50)
    
   
    password_length = get_valid_password_length()
    
    
    print("\n⚡ Compiling cryptographic entropy...")
    secure_password = generate_secure_password(password_length)
    
    
    print("\n" + "-" * 50)
    print(f"✅ Secure Password Generated Successfully:")
    print(f"👉 \033[1;32m{secure_password}\033[0m")  # Prints the password in green text
    print("-" * 50)

if __name__ == "__main__":
    main()