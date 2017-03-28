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
homeworks, a prelim, and a final. You'll be graded according to the following:

* Participation: 10%
* Homeworks:  50% (each homework will count an equal amount)
* Prelim:  20% 
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
| Jan 26 | Intro & one-time-pads | [Slides](slides/intro.pdf) |
| Jan 31  | OTP | [Slides](slides/otp.pdf) |
| Feb 2 |  CTR mode, computational indistinguishability & reductions | [Slides](slides/ctr-mode.pdf) |
| Feb 7 |  Block ciphers | [Slides](slides/ctr-blockcipher.pdf) |
| Feb 9 |  Class cancelled (snow day) | |
| Feb 14 | Block cipher modes, CBC mode | [Slides](slides/symenc.pdf) |
| Feb 16 | Padding oracle attacks | [Slides](slides/padoracle.pdf)  |
| Feb 21 | No Lecture (February break)  |  |
| Feb 23 | Authenticated encryption, Message authentication | [Slides](slides/msgauth.pdf) |
| Feb 28 | Hash functions, HMAC | [Slides](slides/hash.pdf) |
| Mar 2 | Guest lecture: Paul Kehrer |  |
| Mar 7 |  Password-based AEAD | [Slides](slides/pwae.pdf) |
| Mar 9 |  TLS & TLS record layer | [Slides](slides/tls.pdf) |
| Mar 14 | Campus closed   |  |
| Mar 16 | Overview of practice midterm | |
| Mar 21 |  In-class midterm | |
| Mar 23 |  Overview of midterm |   |
| Mar 28 |  Paul's lecture on unit testing  |   |
| Mar 30 | Asymmetric crypto intro  | |
| Apr 4 | No lecture (Spring break) |  |
| Apr 6 | No lecture (Spring break) | |
| Apr 11 | Key exchange & Diffie-Hellman  |  |
| Apr 13 | Hybrid encryption & ElGamal  | |
| Apr 18 | Digital signatures  |  |
| Apr 20 |  Digital signatures & PKI| |
| Apr 25 | OpenPGP | |
| Apr 27 | TextSecure   | |
| May 2 | RNGs  | |
| May 4 | Cryptographic backdoors | |
| May 9 | (Tom traveling) | |

