import os
import hashlib

def get_file_hash(filename):
    with open(filename, "rb") as f:
        content = f.read()

    return hashlib.sha256(content).hexdigest()


hash_value = get_file_hash("note.txt")

print(hash_value)

if not os.path.exists("hash.txt"):
    h = open("hash.txt", "w")
    h.write(hash_value)
    h.close()


h = open("hash.txt", "r")
original_hash = h.read()
h.close()

if original_hash == hash_value:
    print("File has no change")
else:
    print("File modified")