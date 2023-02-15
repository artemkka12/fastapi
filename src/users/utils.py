import bcrypt


def hash_password(password):
    password = password.encode()

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)

    return hashed.decode()
