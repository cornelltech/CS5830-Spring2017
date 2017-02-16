# Homework 2 (CS5830) 
# Trying to implement a length preserving Encryption function.
# 

from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.backends import default_backend
import base64
import binascii

def xor(a,b):
    """
    xors two raw byte streams.
    """
    assert len(a) == len(b), "Lengths of two strings are not same. a = {}, b = {}".format(len(a), len(b))
    return ''.join(chr(ord(ai)^ord(bi)) for ai,bi in zip(a,b))

class MyFeistel:
    def __init__(self, key, num_rounds, backend=None):
        if backend is None:
            backend = default_backend()

        key = base64.urlsafe_b64decode(key)
        if len(key) != 16:
            raise ValueError(
                "Key must be 16 url-safe base64-encoded bytes. Got: {} ({})".format(key, len(key))
            )
        self._num_rounds = num_rounds
        self._encryption_key = key
        self._backend = backend
        self._round_keys = [self._encryption_key \
                            for _ in xrange(self._num_rounds)]
        for i  in xrange(self._num_rounds):
            if i==0: continue
            self._round_keys[i] = self._SHA256hash(self._round_keys[i-1])

    def _SHA256hash(self, data):
        h = hashes.Hash(hashes.SHA256(), self._backend)
        h.update(data)
        return h.finalize()

    def encrypt(self, data):
        assert len(data)%2 == 0, "Supports only balanced feistel at "\
            "this moment. So provide even length messages."

        # TODO - Fill in
        return data

    def decrypt(self, ctx):
        assert len(ctx)%2 == 0, "Supports only balanced feistel at "\
            "this moment. So provide even length ciphertext."
        #TODO - Fill in
        return ctx

    def _prf(self, key, data):
        """Set up secure round function F
        """
        # TODO - set up round function using AES 
        return data

    def _feistel_round_enc(self, data):
        """This function implements one round of Fiestel encryption block.
        """
        # TODO - Implement this function
        return data
    
    def _feistel_round_dec(self, data):
        """This function implements one round of Fiestel decryption block.
        """
        # TODO - Implement this function 
        return data

class LengthPreservingCipher(object):
    #'length' is in bytes here
    def __init__(self, key, length=6):
        self._length = 6
        #TODO 

    def encrypt(self, data):
        # TODO
        return data

    def decrypt(self, data):
        # TODO
        return data

    # TODO - add other functions if required
