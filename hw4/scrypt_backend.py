import struct
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend,MultiBackend
from cryptography.hazmat.primitives import hashes,hmac
from cryptography.hazmat.backends.interfaces import ScryptBackend
import functools
import binascii

#Actual python implementation of Scrypt taken from
#https://github.com/ricmoo/pyscrypt.
#Shim wrapper to make it a pyca backend written by
#Paul Grubbs.


# Python 2
if bytes == str:
    def check_bytes(byte_array):
        return True

    def get_byte(c):
        'Converts a 1-byte string to a byte'
        return ord(c)

    def chars_to_bytes(array):
        'Converts an array of integers to an array of bytes.'
        return ''.join(chr(c) for c in array)

# Python 3
else:
    xrange = range

    def check_bytes(byte_array):
        return isinstance(byte_array, bytes)

    def get_byte(c):
        return c

    def chars_to_bytes(array):
        return bytes(array)


def pbkdf2_single(password, salt, key_length, prf):
    '''Returns the result of the Password-Based Key Derivation Function 2 with
       a single iteration (i.e. count = 1).

       prf - a psuedorandom function

       See http://en.wikipedia.org/wiki/PBKDF2
    '''

    block_number = 0
    result = b''

    # The iterations
    while len(result) < key_length:
        block_number += 1
        result += prf(password, salt + struct.pack('>L', block_number))

    return result[:key_length]


def salsa20_8(B):
    '''Salsa 20/8 stream cypher; Used by BlockMix. See http://en.wikipedia.org/wiki/Salsa20'''

    # Create a working copy
    x = B[:]

    # Expanded form of this code. The expansion is significantly faster but
    # this is much easier to understand
    # ROUNDS = (
    #     (4, 0, 12, 7),   (8, 4, 0, 9),    (12, 8, 4, 13),   (0, 12, 8, 18),
    #     (9, 5, 1, 7),    (13, 9, 5, 9),   (1, 13, 9, 13),   (5, 1, 13, 18),
    #     (14, 10, 6, 7),  (2, 14, 10, 9),  (6, 2, 14, 13),   (10, 6, 2, 18),
    #     (3, 15, 11, 7),  (7, 3, 15, 9),   (11, 7, 3, 13),   (15, 11, 7, 18),
    #     (1, 0, 3, 7),    (2, 1, 0, 9),    (3, 2, 1, 13),    (0, 3, 2, 18),
    #     (6, 5, 4, 7),    (7, 6, 5, 9),    (4, 7, 6, 13),    (5, 4, 7, 18),
    #     (11, 10, 9, 7),  (8, 11, 10, 9),  (9, 8, 11, 13),   (10, 9, 8, 18),
    #     (12, 15, 14, 7), (13, 12, 15, 9), (14, 13, 12, 13), (15, 14, 13, 18),
    # )
    #
    # for (destination, a1, a2, b) in ROUNDS:
    #     a = (x[a1] + x[a2]) & 0xffffffff
    #     x[destination] ^= ((a << b)  | (a >> (32 - b))) & 0xffffffff
    for i in (8, 6, 4, 2):
        a = (x[0] + x[12]) & 0xffffffff
        x[4] ^= ((a << 7) | (a >> 25))
        a = (x[4] + x[0]) & 0xffffffff
        x[8] ^= ((a << 9) | (a >> 23))
        a = (x[8] + x[4]) & 0xffffffff
        x[12] ^= ((a << 13) | (a >> 19))
        a = (x[12] + x[8]) & 0xffffffff
        x[0] ^= ((a << 18) | (a >> 14))
        a = (x[5] + x[1]) & 0xffffffff
        x[9] ^= ((a << 7) | (a >> 25))
        a = (x[9] + x[5]) & 0xffffffff
        x[13] ^= ((a << 9) | (a >> 23))
        a = (x[13] + x[9]) & 0xffffffff
        x[1] ^= ((a << 13) | (a >> 19))
        a = (x[1] + x[13]) & 0xffffffff
        x[5] ^= ((a << 18) | (a >> 14))
        a = (x[10] + x[6]) & 0xffffffff
        x[14] ^= ((a << 7) | (a >> 25))
        a = (x[14] + x[10]) & 0xffffffff
        x[2] ^= ((a << 9) | (a >> 23))
        a = (x[2] + x[14]) & 0xffffffff
        x[6] ^= ((a << 13) | (a >> 19))
        a = (x[6] + x[2]) & 0xffffffff
        x[10] ^= ((a << 18) | (a >> 14))
        a = (x[15] + x[11]) & 0xffffffff
        x[3] ^= ((a << 7) | (a >> 25))
        a = (x[3] + x[15]) & 0xffffffff
        x[7] ^= ((a << 9) | (a >> 23))
        a = (x[7] + x[3]) & 0xffffffff
        x[11] ^= ((a << 13) | (a >> 19))
        a = (x[11] + x[7]) & 0xffffffff
        x[15] ^= ((a << 18) | (a >> 14))
        a = (x[0] + x[3]) & 0xffffffff
        x[1] ^= ((a << 7) | (a >> 25))
        a = (x[1] + x[0]) & 0xffffffff
        x[2] ^= ((a << 9) | (a >> 23))
        a = (x[2] + x[1]) & 0xffffffff
        x[3] ^= ((a << 13) | (a >> 19))
        a = (x[3] + x[2]) & 0xffffffff
        x[0] ^= ((a << 18) | (a >> 14))
        a = (x[5] + x[4]) & 0xffffffff
        x[6] ^= ((a << 7) | (a >> 25))
        a = (x[6] + x[5]) & 0xffffffff
        x[7] ^= ((a << 9) | (a >> 23))
        a = (x[7] + x[6]) & 0xffffffff
        x[4] ^= ((a << 13) | (a >> 19))
        a = (x[4] + x[7]) & 0xffffffff
        x[5] ^= ((a << 18) | (a >> 14))
        a = (x[10] + x[9]) & 0xffffffff
        x[11] ^= ((a << 7) | (a >> 25))
        a = (x[11] + x[10]) & 0xffffffff
        x[8] ^= ((a << 9) | (a >> 23))
        a = (x[8] + x[11]) & 0xffffffff
        x[9] ^= ((a << 13) | (a >> 19))
        a = (x[9] + x[8]) & 0xffffffff
        x[10] ^= ((a << 18) | (a >> 14))
        a = (x[15] + x[14]) & 0xffffffff
        x[12] ^= ((a << 7) | (a >> 25))
        a = (x[12] + x[15]) & 0xffffffff
        x[13] ^= ((a << 9) | (a >> 23))
        a = (x[13] + x[12]) & 0xffffffff
        x[14] ^= ((a << 13) | (a >> 19))
        a = (x[14] + x[13]) & 0xffffffff
        x[15] ^= ((a << 18) | (a >> 14))


    # Add the original values
    for i in xrange(0, 16):
        B[i] = (B[i] + x[i]) & 0xffffffff


def blockmix_salsa8(BY, Yi, r):
    '''Blockmix; Used by SMix.'''

    start = (2 * r - 1) * 16
    X = BY[start:start + 16]                                      # BlockMix - 1

    for i in xrange(0, 2 * r):                                    # BlockMix - 2

        for xi in xrange(0, 16):                                  # BlockMix - 3(inner)
            X[xi] ^= BY[i * 16 + xi]

        salsa20_8(X)                                              # BlockMix - 3(outer)
        aod = Yi + i * 16                                         # BlockMix - 4
        BY[aod:aod + 16] = X[:16]

    for i in xrange(0, r):                                        # BlockMix - 6 (and below)
        aos = Yi + i * 32
        aod = i * 16
        BY[aod:aod + 16] = BY[aos:aos + 16]

    for i in xrange(0, r):
        aos = Yi + (i * 2 + 1) * 16
        aod = (i + r) * 16
        BY[aod:aod + 16] = BY[aos:aos + 16]


def smix(B, Bi, r, N, V, X):
    '''SMix; a specific case of ROMix. See scrypt.pdf in the links above.'''

    X[:32 * r] = B[Bi:Bi + 32 * r]                   # ROMix - 1

    for i in xrange(0, N):                           # ROMix - 2
        aod = i * 32 * r                             # ROMix - 3
        V[aod:aod + 32 * r] = X[:32 * r]
        blockmix_salsa8(X, 32 * r, r)                # ROMix - 4

    for i in xrange(0, N):                           # ROMix - 6
        j = X[(2 * r - 1) * 16] & (N - 1)            # ROMix - 7
        for xi in xrange(0, 32 * r):                 # ROMix - 8(inner)
            X[xi] ^= V[j * 32 * r + xi]

        blockmix_salsa8(X, 32 * r, r)                # ROMix - 9(outer)

    B[Bi:Bi + 32 * r] = X[:32 * r]                   # ROMix - 10


def hmac_prf(k, m, _backend):
    h = hmac.HMAC(k, hashes.SHA256(), _backend)
    h.update(m)
    return h.finalize()
    
class NewScryptBackend(ScryptBackend):
    def __init__(self):
        self.backend = default_backend()

        
    #def hash(self, password, salt, N, r, p, dkLen):
    def derive_scrypt(self, key_material, salt, length, n, r, p):
        password = key_material
        dkLen = length
        N = n
        """Returns the result of the scrypt password-based key derivation function.
        
        Constraints:
        r * p < (2 ** 30)
        dkLen <= (((2 ** 32) - 1) * 32
        N must be a power of 2 greater than 1 (eg. 2, 4, 8, 16, 32...)
        N, r, p must be positive
        """
        
        # This only matters to Python 3
        if not check_bytes(password):
            raise ValueError('password must be a byte array')
        
        if not check_bytes(salt):
            raise ValueError('salt must be a byte array')

        # Scrypt implementation. Significant thanks to https://github.com/wg/scrypt
        if N < 2 or (N & (N - 1)): raise ValueError('Scrypt N must be a power of 2 greater than 1')
        
        # A psuedorandom function
        #prf = lambda k, m: hmac.new(key = k, msg = m, digestmod = hashlib.sha256).digest()
        prf = functools.partial(hmac_prf, _backend=self.backend)
        # convert into integers
        B  = [ get_byte(c) for c in pbkdf2_single(password, salt, p * 128 * r, prf) ]
        B = [ ((B[i + 3] << 24) | (B[i + 2] << 16) | (B[i + 1] << 8) | B[i + 0]) for i in xrange(0, len(B), 4)]

        XY = [ 0 ] * (64 * r)
        V  = [ 0 ] * (32 * r * N)
        
        for i in xrange(0, p):
            smix(B, i * 32 * r, r, N, V, XY)
            
        # Convert back into bytes
        Bc = [ ]
        for i in B:
            Bc.append((i >> 0) & 0xff)
            Bc.append((i >> 8) & 0xff)
            Bc.append((i >> 16) & 0xff)
            Bc.append((i >> 24) & 0xff)
                
        return pbkdf2_single(password, chars_to_bytes(Bc), dkLen, prf)





if __name__=='__main__':
    Tests = [
            dict(password = b'password', salt = b'salt', N = 2, r = 1, p = 1, dkLen = 32, result = '6d1bb878eee9ce4a7b77d7a44103574d4cbfe3c15ae3940f0ffe75cd5e1e0afa'),
            dict(password = b'password', salt = b'salt', N = 32, r = 4, p = 15, dkLen = 128, result = '19f255f7dbcc4128e3467c78c795cb934a82bb813793d2634f6e3adbaee1f54b118fca8b067ab4aad3f6557c716b3734bb93a5cb40500b5e42dc96ccee260fc64d8e660b80e7aecd81c83fefedaf1319b6265e6ef37ca268247052f0b5cac91d14800c1b6f8cb23a28f4620aa0a8e12de88906ec5755a4a643917947a010b7bf'),
            dict(password = b'password', salt = b'salt', N = 128, r = 3, p = 3, dkLen = 45, result = 'bdbefc353d2145625af2d8f86dad13d6bd993daabbb39a740887ff985803a22675284ad4c3ab5f68a779d0b71a'),
            dict(password = b'password', salt = b'salt', N = 256, r = 6, p = 2, dkLen = 100, result = '08d4bd8bc6a0db2d3afb86e14bb3e219c7e067add953576ebc4678f86c85f5bc819de1fe22877c7d98c2ee11fef9f3a1ca0047a079b3ee35152c31d51b8db57f267050255065b933d65edfc65203e9b964c5c54507eba8b990c8c9106274fa105237550a'),
            dict(password = b"You're a master of Karate", salt = b'And friendship for Everyone', N = 1024, r = 1, p = 1, dkLen = 256, result = '3a3cbca04456f6ee5295460171a2a2b27e1c28163999f19ab1e2eeda01e355d904627c6baa185087f99f3fee33e4a9ccad1f4230681d77301d2b4f6543023e090faf6e86431a1071f64b693402ceb485469ef33308af104fb1f87b39ecaf733ebc3d73b184c0914fbc4e8eff90777c60172596de79070418f3c9998b6b60640f1d8f3019904b3e20f2920d26c21daf81d0652ffcaffccf734773e0730900204b56b5bebbfb8c3a31d543f6e3ac5f4e1431a864da87c239eefec8e462d458ee2d214646864e9207e15f66a3782b52bb5158152d757d0ca25d2062235ee76c431e5016b3a52cd5b575e3a26aba95654d5b9a991527f5a19d7275ac4f9889081ee9'),
        ]
    
    for test in Tests:
        multi_backend = MultiBackend([NewScryptBackend(), default_backend()])
        kdf = Scrypt(salt=test['salt'],length=test['dkLen'],n=test['N'],r=test['r'],p=test['p'],backend=multi_backend)
        correct = test['result']
        derived = kdf.derive(test['password'])
        print correct
        print binascii.hexlify(derived)
        print "\n\n"
        assert correct == binascii.hexlify(derived)
