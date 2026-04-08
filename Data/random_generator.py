import random
import string


def generate_user():
    random_str = ''.join(random.choices(string.ascii_lowercase, k=5))
    random_postalcode = ''.join(random.choices(string.digits, k=5))
    random_city = ''.join(random.choices(string.ascii_lowercase, k=5))
    random_state = ''.join(random.choices(string.digits, k=5))

    return {
        "first_name": f"test{random_str}",
        "last_name": f"user{random_str}",
        "dob": "1995-05-15",
        "street": "Test Street",
        "postal_code": f"{random_postalcode}",
        "city": f"{random_city}",
        "state": f"{random_state}",
        "country": "India",
        "phone": f"99999{random.randint(10000, 99999)}",
        "email": "newqa@yopmail.com",
        "password": "Test@123"
    }