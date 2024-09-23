T = int(input())

for _ in range(T):
    C, K = map(int, input().split())  
    ciphertext = input().strip()  

    decrypted_message_C = ''.join(
        chr((ord(char) - (97 if char.islower() else 65) - C) % 26 + (97 if char.islower() else 65))
        if char.isalpha() else char
        for char in ciphertext
        
    )
    print(decrypted_message_C)

    decrypted_message_K = ''.join(
        chr((ord(char) - (97 if char.islower() else 65) - K) % 26 + (97 if char.islower() else 65))
        if char.isalpha() else char
        for char in ciphertext
    )
    print(decrypted_message_K)