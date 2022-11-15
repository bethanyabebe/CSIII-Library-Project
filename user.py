from library import Library
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class User(Library):
    def __init__(self, user, password):
        super().__init__()
        self.user = user
        self.password = password

    @staticmethod
    def check_user(user, password):
        key = b'CFC)H@ERVvcQtTnr'

        def encrypt(msg):
            e_cipher = AES.new(key, AES.MODE_ECB)
            encrypted = e_cipher.encrypt(pad(msg.encode(), 32))
            return encrypted.hex()

        infile = open("user.txt")
        for line in infile:
            temp = line.strip("\n")
            if temp.split(",")[0] == user and str(temp.split(",")[1]) == str(encrypt(password)):
                return True
        return False
