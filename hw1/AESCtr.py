from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import binascii
import os


class AESCtr:
  def __init__(self, key, backend=None):
    if backend is None:
      backend = default_backend()

      key = base64.urlsafe_b64decode(key)
      if len(key) != 16:
        raise ValueError("AES key must be 16 btyes long and url-safe base64-encoded."  
              "Got: {} ({})".format(key, len(key)))
      self._encryption_key = key
      self._backend = backend
      self._block_size_bytes = algorithms.AES.block_size / 8    # in bytes
      self._nonce_size = self._block_size_bytes / 2             # in bytes

  def _nonced_counters(self, nonce, numblocks):
    """Returns the nonced 16 byte counter required for ctr mode"""
    for ctr in xrange(numblocks):
      yield nonce + struct.pack('>Q', ctr)

  def _encipher_one_block(self, data):
    encryptor = Cipher(algorithms.AES(self._encryption_key),modes.ECB(),self._backend).encryptor()
    return encryptor.update(data) + encryptor.finalize()

  def encrypt(self, data):  
    """ This function takes a byte stream @data and outputs the  ciphertext """
    if not isinstance(data, bytes):
      raise TypeError("data must be bytes.")
    nonce = os.urandom(self._nonce_size)
    ctx = ""

    # TODO: Fill in this function

    return ctx

  def decrypt(self, ctx):
    """ This function decrypts a ciphertext encrypted using AES-CTR mode.  """ 
    data = ""

    # TODO: Fill in this function.

    return data



