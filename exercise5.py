class VigenereCipher:
    """
       VigenereCipher class.
 
       Attributes:
           keyword (str): The word to be used as the key
           offset (int): The ASCII value of the letter 'A'. A static utility attribute to help you calculate
                a letter's position in the alphabet from 0 (A) to 25 (Z).
    """
    offset = ord('A')
 
    def __init__(self, keyword: str):
        self.keyword = keyword.upper()
 
    def __shift_letter(self, letter: str, shift: int, forward: bool):
        """
        Private method to shift a letter a number of positions forward or backward in the alphabet.
        """
        position = ord(letter) - self.offset          # 'A'->0 ... 'Z'->25
        if forward:
            new_position = (position + shift) % 26    # wrap past Z back to A
        else:
            new_position = (position - shift) % 26    # wrap before A back to Z
        shifted_letter = chr(new_position + self.offset)
        return shifted_letter
 
    def __generate_shift_list(self, plaintext_length: int):
        """
        Private method to generate a list of integers. Each element is the shift to encrypt the
        plaintext letter at the same position.
        """
        shift_list = []
        for i in range(plaintext_length):
            key_letter = self.keyword[i % len(self.keyword)]   # repeat keyword, handles partial repeats
            shift_list.append(ord(key_letter) - self.offset)
        return shift_list
 
    def __clean(self, text: str):
        """Uppercase the text and keep only the letters A-Z."""
        return ''.join(c for c in text.upper() if 'A' <= c <= 'Z')
 
    def encrypt(self, plaintext: str):
        """
        Encrypts a plaintext string.
        """
        cleaned = self.__clean(plaintext)
        shifts = self.__generate_shift_list(len(cleaned))
        ciphertext = ''
        for i in range(len(cleaned)):
            ciphertext += self.__shift_letter(cleaned[i], shifts[i], True)
        return ciphertext
 
    def decrypt(self, ciphertext: str):
        """
        Decrypts a ciphertext string
        """
        cleaned = self.__clean(ciphertext)
        shifts = self.__generate_shift_list(len(cleaned))
        plaintext = ''
        for i in range(len(cleaned)):
            plaintext += self.__shift_letter(cleaned[i], shifts[i], False)
        return plaintext
 
 
def main():
    vig_cipher = VigenereCipher('smarties')
    ciphertext = vig_cipher.encrypt("The quick brown fox jumps over the lazy dog")
    plaintext = vig_cipher.decrypt(ciphertext)
    assert plaintext == 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'
 
 
if __name__ == "__main__":
    main()