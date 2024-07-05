"""
使用一種簡單的加密方法：將字串中的每個字元，轉換成其在英文字母表中的位置（
A為1，B為2，以此類推），然後將該位置乘以密碼數字1357得到新的位置。
加密後的字串就是用這些新位置對應的字元組成的。

解密的方式則相反，首先將每個字元轉換回其在英文字母表中的位置，然後再除以密碼
數字1357得到原來的位置。最後，用這些原始位置對應的字元組成解密後的字串。
"""

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            decrypted_text += decrypted_char
    return decrypted_text

# 加密字串"dlin"
encrypted_string = encrypt("dlin", 1357)
print(f'Encrypted string: {encrypted_string}')

# 解密字串
decrypted_string = decrypt(encrypted_string, 1357)
print(f'Decrypted string: {decrypted_string}')
