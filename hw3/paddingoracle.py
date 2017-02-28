
import os
from cryptography.hazmat.primitives import hashes, padding, ciphers
from cryptography.hazmat.backends import default_backend

import base64
import binascii

def xor(a,b):
    """
    xors two raw byte streams.
    """
    assert len(a) == len(b), "Lengths of two strings are not same. a = {}, b = {}".format(len(a), len(b))
    return ''.join(chr(ord(ai)^ord(bi)) for ai,bi in zip(a,b))

def split_into_blocks(msg, l):
    while msg:
        yield msg[:l]
        msg = msg[l:]

class PaddingOracle(object):
    def __init__(self, msg_len=0):
        self._backend = default_backend()
        self._block_size_bytes = ciphers.algorithms.AES.block_size/8
        self._key = os.urandom(self._block_size_bytes)
        if msg_len>0:
            self._msg = os.urandom(msg_len)
        else:
            self._msg = "Top-secret message!!!!"
        self._ciphertext = ''
        
    def test(self, msg):
        """
        Test whether your attack succceeded or not!
        """
        return msg in [self._msg, self._padded_msg]

    def ciphertext(self):
        return self.setup()
    
    def setup(self):
        if not self._ciphertext:
            padder = padding.PKCS7(ciphers.algorithms.AES.block_size).padder()
            self._padded_msg = padded_msg = padder.update(self._msg) + padder.finalize()
            # print padded_msg.encode('hex')
            iv = os.urandom(self._block_size_bytes)
            encryptor = ciphers.Cipher(ciphers.algorithms.AES(self._key),
                                       ciphers.modes.CBC(iv),
                                       self._backend).encryptor()
            self._ciphertext = iv + encryptor.update(padded_msg) + encryptor.finalize()
        return self._ciphertext

    @property
    def block_length(self):
        return self._block_size_bytes
    
    def encrypt(self, msg):
        raise Exception("Encrypt is not allowed in this oracle!")

    def decrypt(self, ctx):
        iv, ctx = ctx[:self._block_size_bytes], ctx[self._block_size_bytes:]
        unpadder = padding.PKCS7(ciphers.algorithms.AES.block_size).unpadder()
        decryptor = ciphers.Cipher(ciphers.algorithms.AES(self._key),
                                   ciphers.modes.CBC(iv),
                                   self._backend).decryptor()        
        padded_msg = decryptor.update(ctx) + decryptor.finalize()
        try:
            msg = unpadder.update(padded_msg) + unpadder.finalize()
            return True  # Successful decryption
        except ValueError:
            return False  # Error!!



################################################################################
## The following code provides API to access padding oracle server.
################################################################################

from urllib2 import urlopen
import json

url = 'https://paddingoracle.herokuapp.com/'

class PaddingOracleServer(object):
    def __init__(self, msg_len=0):
        self._backend = default_backend()
        self._block_size_bytes = ciphers.algorithms.AES.block_size/8
        pass

    @property
    def block_length(self):
        return self._block_size_bytes

    def decrypt(self, ctx):
        #print "In decrypt!!!"
        dec_url = url + "decrypt/{}".format(base64.urlsafe_b64encode(ctx))
        ret = json.load(urlopen(dec_url))
        return ret['return'] == 0

    def ciphertext(self):
        ctx_url = url + "ctx"
        ret = json.load(urlopen(ctx_url))
        return base64.urlsafe_b64decode(str(ret['ctx']))

    def test(self, msg):
        test_url = url + "test/{}".format(base64.urlsafe_b64encode(msg))
        ret = json.load(urlopen(test_url))
        return ret['return'] == 0

    def setup(self):
        return self.ciphertext()
