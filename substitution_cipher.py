import random

alphabet = ""
for i in range(32,127):
    alphabet += chr(i)
print(alphabet)


key = ""
for n in alphabet:
    key = n + key
print(key)


def encrypt(message):
    result = ""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

def decrypt(message):
    result = ""
    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result


unencrypted_message = "encryption is fun"
encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)

with open('substitution_sample_run.txt', 'w') as f:
    f.write(encrypted_message + "\n")
    f.write(decrypt(encrypted_message))
            
