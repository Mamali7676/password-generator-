from main.src.generator import generate_password

def test_password_length():
    password = generate_password(10)
    assert len(password) == 10, "Password length mismatch!"

if __name__ == "__main__":
    test_password_length()
    print("✅ All tests passed successfully!")
