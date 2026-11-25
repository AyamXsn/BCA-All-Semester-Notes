# Cryptography Basics

## 1. Cryptography
Cryptography uses mathematical techniques to protect information and support properties such as confidentiality, integrity, authentication, and non-repudiation in suitable protocols.

## 2. Symmetric encryption
The same secret key is used to encrypt and decrypt. It is efficient for bulk data, but secure key distribution is a challenge.

## 3. Asymmetric cryptography
A public/private key pair supports operations such as key establishment and digital signatures. Public-key techniques are generally more computationally expensive than symmetric encryption.

## 4. Hash functions
A cryptographic hash maps input to a fixed-size digest. A secure hash is designed to resist preimage, second-preimage, and collision attacks. Hashing is not encryption and has no decryption key.

## 5. Digital signatures
A signature scheme lets a signer use a private key to sign data and others use the corresponding public key to verify it. It can support authenticity and integrity.

## 6. Password storage
Passwords should be stored using a dedicated password-hashing scheme with salts and suitable work factors, not plain text or a fast general-purpose hash alone.

## 7. Exercise
Explain the difference between encryption, hashing, and digital signatures.
