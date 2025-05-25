print("************This is a Caesar cipher python program******************")
choice = input("Enter encrypt if you want to encode or decrypt to decode:")

if (choice.lower() == "encrypt"):
    message = input("Enter the message which you want to encode:")
    shift = int(input("Enter the place by which you want to shift the number:"))
    for i in range(len(message)):
        c = ord(message[i])
        if (65 <= c <= 90):`
            if (c + shift <= 90):
                message = message[:i] + chr(c + shift) + message[i + 1:]
            else:
                shifted_char = chr((c - 65 + shift) % 26 + 65)
                message = message[:i] + shifted_char + message[i + 1:]
        elif (97 <= c <= 122):
            if (c + shift <= 122):
                message = message[:i] + chr(c + shift) + message[i + 1:]
            else:
                shifted_char = chr((c - 97 + shift) % 26 + 97)
                message = message[:i] + shifted_char + message[i + 1:]
        else:
            message = message[:i] + message[i] + message[i + 1:]

elif (choice.lower() == "decrypt"):
    message = input("Enter the message which you want to decode:")
    shift = int(input("Enter the place by which you want to shift the number:"))
    for i in range(len(message)):
        c = ord(message[i])
        if (65 <= c <= 90):
            if (c - shift >= 65):
                message = message[:i] + chr(c - shift) + message[i + 1:]
            else:
                shifted_char = chr((c - 65 - shift) % 26 + 65)
                message = message[:i] + shifted_char + message[i + 1:]
        elif (97 <= c <= 122):
            if (c - shift >= 97):
                message = message[:i] + chr(c - shift) + message[i + 1:]
            else:
                shifted_char = chr((c - 97 - shift) % 26 + 97)
                message = message[:i] + shifted_char + message[i + 1:]
        else:
            message = message[:i] + message[i] + message[i + 1:]

else:
    print("Invalid choice! Please enter 'encrypt' or 'decrypt'.")

print(message)
