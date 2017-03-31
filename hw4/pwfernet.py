import scrypt_backend

#“Small” (byte 0x00): n=2^16, r=8, p=1
#“Medium” (byte 0x01): n=2^18, r=8, p=1
#“Large” (byte 0x02): n=2^20, r=8, p=1
#“Extra large” (byte 0x03): n=2^20, r=16, p=2
class Sizes:
    small = (2**16, 8, 1)
    medium = (2**18, 8, 1)
    large = (2**20, 8, 1)
    xlarge = (2**20, 16, 2)

class PWFernet:
    def __init__(self, pw):
        self.password = pw
        self.backend = MultiBackend([NewScryptBackend(), default_backend()])
        
    def encrypt(self, message):
        pass
    
    def decrypt(self, ciphertext):
        pass
