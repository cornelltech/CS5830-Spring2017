# Syllabus for CS 5830

Welcome to CS 5830, Cryptography. We will be studying cryptography and how to use it in practice. By the end of  the course you should understand not only the basics of cryptography, but how to implement suitable cryptographic algorithms within broader projects. You'll also get a taste of modern theoretical cryptography here and there, but this course will not focus on theory and no higher-level mathematics will be needed. 

A key aspect of the course will be implementing cryptographic schemes, as well as showing how to break poorly designed or implemented schemes. A final project for the course will consist of some non-trivial cryptographic feature being implemented in support of a larger project (e.g., a startup project). 

Instructor: Tom Ristenpart (https://rist.tech.cornell.edu)
TA: Rahul Chatterjee (https://www.cs.cornell.edu/~rahul/)


### Pre-requisites

Students should have programming experience (we will be focusing on Python),
understand basic probability, know binary representations (ASCII), operations on bit strings (XOR), have some background on computer networking, file systems, etc. If in doubt shoot the instructor an email.



### Requirements

The class will involve a combination of lectures, in-class group exercises,
homeworks,  a course project, and a final. You'll be graded according to the following:

* Participation: 20%
* Homeworks:  30% (each homework will count an equal amount)
* Project:  30% 
* Final:  20% 

### Background reading

The following books should be helpful, but none are required if you don't want to spend the money:

* [Cryptography 101 by Houtven](https://www.crypto101.io/). Free, but not   complete. Feel free to send helpful feedback to the author.

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
| Jan 28 | Intro & one-time-pads | |
| Feb 2  | Block ciphers | HW0 (CTR mode) released. |
| Feb 4 |  Block ciphers from block ciphers |  |
| Feb 9 | Usage of crypto discussion | HW0 due. HW1 (length preserving cipher)  released. |
| Feb 11 | Guest lecture TBA | |
| Feb 16 | No lecture  (February break) | |
| Feb 18 | Insecure symmetric encryption |  HW1 due. HW2 (padding oracle attack) released. |
| Feb 23 | PRFs & message authentication |  |
| Feb 25 | Authenticated encryption | |
| Mar 1 | AEAD & hash functions |  |
| Mar 3 | Password handling | HW2 due. HW3 (AEAD) released. |
| Mar 8 | Project proposal discussion  | |
| Mar 10 | TLS & TLS record layer | |
| Mar 15 | Public-key encryption & key transport |  |
| Mar 17 | RSA | |
| Mar 22 | Key exchange & Diffie-Hellman | |
| Mar 24 | Digital signatures |  HW3 due. |
| Mar 29 | No lecture (Spring break) |  Enjoy the break and think about the project. |
| Mar 31 | No lecture (Spring break) | |
| Apr 5 | Digital signatures & PKI | HW4 released (TLS setup) |
| Apr 7 | Digital signatures & PKI | |
| Apr 12 | Hybrid encryption & ElGamal | HW4 due. HW5 (Public-key encryption) released. |
| Apr 14 | OpenPGP & TextSecure  | |
| Apr 19 | Class cancelled |  |
| Apr 21 | In-class HW5 spec writing | |
| Apr 26 | Guest lecture (Vitaly Shmatikov) | |
| Apr 28 | RNGs  | |
| May 3 | Cryptographic backdoors | |
| May 5 | In-class project summary presentations | |
| May 10 | TBA  | |

