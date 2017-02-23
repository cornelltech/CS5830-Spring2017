# Syllabus for CS 5830

Welcome to CS 5830, Cryptography. We will be studying cryptography and how to
use it in practice. By the end of  the course you should understand not only the
basics of cryptography, but how to implement suitable cryptographic algorithms
within broader projects. You'll also get a taste of modern theoretical
cryptography here and there, but this course will not focus on theory and no
higher-level mathematics will be needed. 

A key aspect of the course will be implementing cryptographic schemes, as well
as showing how to break poorly designed or implemented schemes. Some homeworks
will target feature requests in a widely used cryptography library, bonus points
will be awarded for pull-worthy code.


Instructor: Tom Ristenpart (https://rist.tech.cornell.edu)
TA: Paul Grubbs (https://www.cs.cornell.edu/~paulgrubbs/)


### Pre-requisites

Students should have programming experience (we will be focusing on Python),
understand basic probability, know binary representations (ASCII), operations on
bit strings (XOR), have some background on computer networking, file systems,
etc. If in doubt shoot the instructor an email.



### Requirements

The class will involve a combination of lectures, in-class group exercises,
homeworks, a midterm, and a final. You'll be graded according to the following:

* Participation: 10%
* Homeworks:  50% (each homework will count an equal amount)
* Project:  20% 
* Final:  20% 

There will be several opportunities for extra credit, as well.

### Background reading

The following books should be helpful, but none are required if you don't want to spend the money:

* [Cryptography 101 by Houtven](https://www.crypto101.io/). Free, but not complete. Feel free to send helpful feedback to the author.

* [Cryptography Engineering by Ferguson, Schneier, and Kohno](https://www.schneier.com/books/cryptography_engineering/). A gentle
  introduction to cryptography.

* [Modern Cryptography by Katz and Lindell](http://www.cs.umd.edu/~jkatz/imc.html). A formal treatment of cryptography.
  We will make reference to, but not go into detail on, topics they treat in
  more detail.


## Lecture schedule

A very preliminary schedule is below to give a taste of the scope of
what we're hoping to cover.  Homeworks will be due on the due date by
11:59:59pm EST. You can use in total 3 late days throughout the semeseter. 



| Date |  Topic  |  Note |
|------|---------|--------|
| Jan 26 | Intro & one-time-pads | |
| Jan 31  | OTP |  |
| Feb 2 |  CTR mode, computational indistinguishability & reductions |  |
| Feb 7 |  Block ciphers |  |
| Feb 9 |  Class cancelled (snow day) | |
| Feb 14 | Block cipher modes, CBC mode | |
| Feb 16 | Padding oracle attacks |   |
| Feb 21 | No Lecture (February break)  |  |
| Feb 23 | Authenticated encryption, Message authentication | |
| Feb 28 | Hash functions, HMAC |  |
| Mar 2 | Guest lecture: Paul Kehrer |  |
| Mar 7 |  TLS & TLS record layer | |
| Mar 9 |  In-class midterm | |
| Mar 14 | Public-key encryption & key transport  |  |
| Mar 16 |  RSA| |
| Mar 21 |  Key exchange & Diffie-Hellman| |
| Mar 23 | Hybrid encryption & ElGamal  |   |
| Mar 28 | Digital signatures |   |
| Mar 30 | Digital signatures & PKI | |
| Apr 4 | No lecture (Spring break) |  |
| Apr 6 | No lecture (Spring break) | |
| Apr 11 | OpenPGP  |  |
| Apr 13 |  TextSecure  | |
| Apr 18 | RNGs |  |
| Apr 20 | Cryptographic backdoors | |
| Apr 25 | | |
| Apr 27 |   | |
| May 2 | (Tom traveling) | |
| May 4 |  | |
| May 9 | (Tom traveling) | |

