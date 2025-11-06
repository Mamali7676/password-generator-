from generator import generate_password

def main():
    print("🔐 Password Generator 🔐")
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print(f"Your random password: {password}")

if __name__ == "__main__":
    main()
