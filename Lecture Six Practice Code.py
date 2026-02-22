"""
REQ-12:
System shall hash user passwords before storing them.
This example demonstrates Architecture → Code → Test traceability.
"""

import hashlib

class AuthService:
    """
    Authentication/Identity Module
    Traceability:
    REQ-12 -> AuthService -> hash_password() -> verify_password()
    """
    # REQ-12
    def hash_password(self, plain_password: str) -> str:
        """
        Hash password using SHA-256 (built-in library).
        """
        if not isinstance(plain_password, str) or plain_password == "":
            raise ValueError("plain_password must be a non-empty string")

        return hashlib.sha256(plain_password.encode()).hexdigest()

    # REQ-12
    def verify_password(self, plain_password: str, stored_hash: str) -> bool:
        """
        Verify plaintext password against stored hash.
        """
        return self.hash_password(plain_password) == stored_hash

# -----------------------
# Simple Test Execution
# -----------------------

def run_tests():
    auth = AuthService()

    original = "abc123"
    hashed = auth.hash_password(original)

    print("Original:", original)
    print("Hashed  :", hashed)
    print()

    # Test 1: Hash should not equal original
    assert hashed != original
    print("Test 1 Passed: Hash is not equal to original")

    # Test 2: Correct password verifies
    assert auth.verify_password(original, hashed) is True
    print("Test 2 Passed: Correct password verification")

    # Test 3: Incorrect password fails
    assert auth.verify_password("wrongpass", hashed) is False
    print("Test 3 Passed: Incorrect password verification")

    print("\nAll tests passed successfully.")


# Run tests automatically
if __name__ == "__main__":
    run_tests()
