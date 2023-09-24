# Password Generator

The `PasswordGenerator` class is a Python tool for generating both simple and complex passwords based on specified criteria.

## Usage

Import the `PasswordGenerator` class in your Python script:

```python
from password_generator import PasswordGenerator
```

### 1. Create an instance of the PasswordGenerator class with optional criteria:

```python
password_generator = PasswordGenerator()
```
You can customize the password criteria by providing values to the constructor. If not specified, default values are used.
   
### 2. Generate a simple password:

```python
simple_password = password_generator.generate_simple_password()
```

### 3. Generate a complex password:

```python
complex_password = password_generator.generate_complex_password()
```

### 4. Print the generated passwords:

```python
print("Simple Password:", simple_password)
print("Complex Password:", complex_password)
```

## Configuration Options

The PasswordGenerator class allows you to customize the following criteria:

```
min_length: Minimum length of the password (default: 8)
max_length: Maximum length of the password (default: 16)
min_lowercase: Minimum number of lowercase characters (default: 2)
max_lowercase: Maximum number of lowercase characters (default: 4)
min_uppercase: Minimum number of uppercase characters (default: 2)
max_uppercase: Maximum number of uppercase characters (default: 4)
min_numerics: Minimum number of numeric characters (default: 1)
max_numerics: Maximum number of numeric characters (default: 3)
min_special: Minimum number of special characters (default: 1)
max_special: Maximum number of special characters (default: 2)
```

## Example usage:

```python
password_generator = PasswordGenerator()
simple_password = password_generator.generate_simple_password()
complex_password = password_generator.generate_complex_password()

print("Simple Password:", simple_password)
print("Complex Password:", complex_password)
```
