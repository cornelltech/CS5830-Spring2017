import scrypt_backend


# “Small” (byte 0x00): n=2^10, r=4, p=1
# “Medium” (byte 0x01): n=2^10, r=6, p=1
# “Large” (byte 0x02): n=2^11, r=8, p=1
# “Extra large” (byte 0x03): n=2^12, r=8, p=2


class Sizes:
    small = (2**10, 4, 1)
    medium = (2**10, 6, 1)
    large = (2**11, 8, 1)
    xlarge = (2**12, 8, 2)

class PWFernet:
    def __init__(self, pw):
        self.password = pw
        self.backend = MultiBackend([NewScryptBackend(), default_backend()])
        
    def encrypt(self, message):
        pass
    
    def decrypt(self, ciphertext):
        pass
