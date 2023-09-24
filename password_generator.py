import random
import string


class PasswordGenerator:
    def __init__(self, min_length=8, max_length=16, min_lowercase=2, max_lowercase=4, min_uppercase=2, max_uppercase=4, min_numerics=1, max_numerics=3, min_special=1, max_special=2):
        self.min_length = min_length
        self.max_length = max_length
        self.min_lowercase = min_lowercase
        self.max_lowercase = max_lowercase
        self.min_uppercase = min_uppercase
        self.max_uppercase = max_uppercase
        self.min_numerics = min_numerics
        self.max_numerics = max_numerics
        self.min_special = min_special
        self.max_special = max_special

    def generate_simple_password(self):
        """ Generate Simple Password """
        length = random.randint(self.min_length, self.max_length)
        password = []

        for _ in range(length):
            category = random.choice([string.ascii_lowercase, string.ascii_uppercase, string.digits])
            password.append(random.choice(category))

        random.shuffle(password)
        return ''.join(password)

    def generate_complex_password(self):
        """ Generate Complex Password """
        if self.min_length < (self.min_lowercase + self.min_uppercase + self.min_numerics + self.min_special) or self.max_length < (self.min_lowercase + self.min_uppercase + self.min_numerics + self.min_special):
            raise ValueError("Invalid criteria. Minimum length is not enough to satisfy character requirements.")

        length = random.randint(self.min_length, self.max_length)
        password = []

        for _ in range(self.min_lowercase):
            password.append(random.choice(string.ascii_lowercase))

        for _ in range(self.min_uppercase):
            password.append(random.choice(string.ascii_uppercase))

        for _ in range(self.min_numerics):
            password.append(random.choice(string.digits))

        for _ in range(self.min_special):
            password.append(random.choice(string.punctuation))

        remaining_length = length - len(password)

        for _ in range(remaining_length):
            category = random.choice([string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation])
            password.append(random.choice(category))

        random.shuffle(password)
        return ''.join(password)


if __name__ == '__main__':
    # Create Class Object
    password_generator = PasswordGenerator()

    # Generate Simple Password
    simple_password = password_generator.generate_simple_password()

    # Generate Complex Password
    complex_password = password_generator.generate_complex_password()

    print("Simple Password:", simple_password)
    print("Complex Password:", complex_password)
