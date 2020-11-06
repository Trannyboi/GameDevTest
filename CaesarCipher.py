# The String to be Encrypted/Decrypted:
message = input('Enter your message:\n')

# The Encryption/Decryption Key:
key = int(input('Enter key:\n'))

# Whether the Program Encrypts or Decrypts:
mode = input('encrypt or decrypt:\n')  # Set to either 'encrypt' or 'decrypt'.

# Every Possible Symbol that can be Encrypted/Decrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?,.'

# Store the Encrypted/Decrypted form of the Message:
translated = ''

for symbol in message:
    # Note: Only Symbols in the SYMBOLS String can be Encrypted/Decrypted
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform Encryption/Decryption
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle Wraparound, if Needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the Symbol without Encrypting/Decrypting:
        translated = translated + symbol

# Output the Translated String:
print(translated)