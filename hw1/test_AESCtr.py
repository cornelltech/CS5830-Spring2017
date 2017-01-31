#!/usr/bin/python 

from AESCtr import AESCtr
import pytest
import base64
import os

def test_basic():
  key = base64.urlsafe_b64encode(os.urandom(16))

  aes = AESCtr(key)
  txt = b'A great Secret message'*12  # To make it larger than 128-bit
  ctx = aes.encrypt(txt)
  dtxt = aes.decrypt(ctx)
  assert dtxt==txt, "The decrypted text is not the same as the original text"

# TODO: Fill in more tests of AESCtr

