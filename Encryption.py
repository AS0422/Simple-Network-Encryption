# Simple XOR encryption function
def Encryption(string, key):
    
    string =[ord(char)for char in string]
    key = [ord(char) for char in key]

    encrypt = [string ^ key for string, key in zip(string, key * (len(string) // len(key) + 1))]
    message = ''.join(chr(byte) for byte in encrypt)

    return message