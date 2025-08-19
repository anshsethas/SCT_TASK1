# SkillCraft Technology Internship

## Task 01 - Caesar Cipher

###  Task Objective
The goal of this task is to implement the **Caesar Cipher Algorithm**, one of the most fundamental and classical encryption techniques in cryptography.  
The Caesar Cipher works by shifting each letter in a given message by a fixed number of positions in the alphabet.  
For example, with a shift of 3:
- `A` becomes `D`
- `B` becomes `E`
- `Z` becomes `C`

This project demonstrates how encryption and decryption can be performed using simple mathematical operations on character codes.

---

### Implementation Details
- Language Used: **Python**
- Files Included:
  - `task1.py` 鈫� Python program containing Caesar Cipher implementation.
  - `README.md` 鈫� Documentation file explaining the project.

The program includes two functions:
1. **encrypt(text, shift)**  
   - Encrypts a given message by shifting letters forward by the shift value.
2. **decrypt(text, shift)**  
   - Decrypts the given encrypted message by shifting letters backward.

---

### How It Works
- A fixed message (`HELLO WORLD`) and a fixed shift value (`3`) have been used for demonstration.  
- The text is processed character by character:
  - Alphabetic characters are shifted within their range (`A-Z` or `a-z`).
  - Non-alphabetic characters (like spaces, numbers, punctuation) remain unchanged.
- The encrypted text can then be decrypted back to the original using the same shift.

---

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/anshsethas/SCT_PY_1.git
   cd SCT_PY_1
