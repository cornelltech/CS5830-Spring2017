# Public-key encryption
```json
Deadline: 23:59:59, May 17, 2016 
```
We want to build an application layer public key encryption scheme that will allow users to send messages asynchronously with others without a pre-shared secret key.  A typical way to do this is using a hybrid of public-key and symmetric-key encryption schemes. The symmetric encryption portion of this can utilize our existing Fernet2 encryption scheme. While for the public-key part of it, we shall use one or more asymmetric encryption schemes supported by the `cryptography` library. Let call this encryption scheme `PKFernet`.

### Functionality
We expect the following basic functionalities from `PKFernet`. 
The scheme allows users to `encrypt` and `decrypt` messages. The `encryption` routine should first sign the message using the sender’s secret key for signing, and then encrypt the signed message using the public key for encryption of the recipient. The recipient should be able `decrypt` and verify the message using his private key for encryption and public for signing of the sender respectively.
`PKFernet` should be cryptographically agile, i.e., it should be able to adapt to new cryptographic primitives. Users might choose to use different cryptographic primitives, and may or may not choose to be backward compatible. But the scheme should gracefully handle (process or reject) different versions of ciphertexts.

### Specification?
As this encryption scheme explicitly attempts to enable a global communication of encrypted messages, we have to decide on a global protocol and specification. We shall assume that we already have a medium of communication, and only need to decide on the specification of the encryption scheme. However, remember that the specification should be without ambiguities, should be democratically selected, and every one must follow it. 

A draft specification will be made available on Slack. It is from last year’s class, and while it was pretty complete, it still had some problems. Please review the draft and make suggestions by adding comments. One way to do this is think about how you’ll implement the draft, and see where ambiguities come up --- any time you encounter an ambiguity leave a comment in the appropriate location of the draft. We can then refine the spec; *refinements will be made only until May 10th*. All discussion of the draft will be among the whole group; individuals should work on their own implementations and not share code. 

The final implementations will be cross-tested, that is an encrypted message
from one person’s implementation will be decrypted using another person’s
implementation.  We will set up another shared Google spreadsheet for sample
plaintext-ciphertexts pairs from each individual.



### Points breakdown
Here is the (high-level) point breakup for the HW5:
* Earn 30 points for helping refine the detailed specification for the encryption scheme and message format, and writing tests for your implementation.
* You may get docked points for violating specifications that we decide collectively.
* You will get 50 points for implementing the scheme that works with at least itself--it should pass the basic functionality tests.
* Finally, 20 points will awarded if the scheme works with at least two other implementations (including the TA’s).
* Extra credit: 10 points for supporting each additional cryptographic primitives capped at 50 points. For example, Encryption (key encapsulation part) if you can handle ECC based DH,  and RSA, you will get 20 extra points. If you support ECDSA, DSA, and RSA-based signature schemes, you will get 20 extra points. If you can support different ECC curves (the ones supported by cryptography.io), and different hashing algorithms, you will earn 10 more marks.



### Shared documents
* [Specification doc](https://docs.google.com/document/d/1DFQ70_JkO3vuxvjTK4A7mBQkdwQrgy_Kmbn9tjoFcb4/edit)  
Use this doc to discuss about the common specification for the encryption scheme. 

* TBA soon: spreadsheet for ciphertext compatibility checking






