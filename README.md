# File Integrity Checker

A simple Python-based File Integrity Checker that uses **SHA-256 hashing** to detect changes made to a file.

This project demonstrates the basics of file integrity monitoring, hashing, and file handling in Python.

## Features

- Generates a SHA-256 hash of a file.
- Stores the original hash in `hash.txt`.
- Compares the current hash with the saved original hash.
- Detects whether the file has been modified.
- Automatically creates `hash.txt` if it does not exist.
- Uses a reusable function to calculate file hashes.

## Technologies Used

- **Python**
- **hashlib** – For SHA-256 hash generation.
- **os** – For checking whether the hash file exists.
- **Git & GitHub** – For version control.

## How It Works

1. The program reads `note.txt`.
2. It generates a SHA-256 hash of the file content.
3. If `hash.txt` does not exist, the program creates it and saves the original hash.
4. On subsequent runs, the program reads the saved hash.
5. It compares the original hash with the newly generated hash.
6. The program displays whether the file has changed.

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/USERNAME/File-Integrity-Checker.git
```

Replace `USERNAME` with your GitHub username.

**2. Open the project folder**

```bash
cd File-Integrity-Checker
```

**3. Run the Python program**

```bash
python detail.py
```

Make sure Python is installed and `note.txt` exists in the project folder.

## Example Output

**When the file has not changed:**

```text
File has no change
```

**When the file has been modified:**

```text
File modified
```

## Project Structure

```text
File-Integrity-Checker/
├── detail.py
├── note.txt
├── .gitignore
└── README.md
```

The `hash.txt` file is generated automatically and excluded from Git tracking using `.gitignore`.

## What I Learned

Through this project, I practiced:

- File handling in Python
- SHA-256 hashing
- Functions and return values
- Conditional statements
- File integrity verification
- Git and GitHub version control

## Future Improvements

- Support integrity checking for multiple files.
- Allow users to enter a filename.
- Generate file integrity reports.

---

**Project Type:** Python Mini Project | Cybersecurity Fundamentals
