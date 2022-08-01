import math

class SubstitutionCipher:
    def __init__(self):
        pass
    def encrypt(self,key,plainText):
        print("Encrypting using substitution...")
        cipherText = ""
        for letter in plainText:
            cipherText=cipherText+chr(ord(letter)+len(key))
        return cipherText
    
    def decrypt(self,key,cipherText):
        print("Decrypting using substitution...")
        plainText = ""
        for letter in cipherText:
            plainText=plainText+chr(ord(letter)-len(key))
        return plainText

class TranspositionCipher:
    def __init__(self):
        pass
    def encrypt(self,key,plainText):
        cipherText = ""
        ind = 0
        orderedKey = sorted(list(key))
        plainTextList = list(plainText)
        columns = len(key)
        rows = math.ceil(len(plainText)/columns)
        plainTextList.extend("_"*(int((rows * columns) - len(plainText))))
        matrix = [plainTextList[i:i+columns] for i in range(0, len(plainTextList), columns)]
        for _ in range(columns):
            i = key.index(orderedKey[ind])
            cipherText += "".join([rows[i] for rows in matrix])
            ind += 1
        return cipherText

    def decrypt(self,key,cipherText):
        plainText = ""
        ind = 0
        orderedKey = sorted(list(key))
        index=0
        cipherTextList = list(cipherText)
        columns = len(key)
        row = int(math.ceil(len(cipherText) / columns))
        dec_matrix = []
        for _ in range(row):
            dec_matrix += [[None] * columns]
        for _ in range(columns):
            curr_idx = key.index(orderedKey[ind])
    
            for j in range(row):
                dec_matrix[j][curr_idx] = cipherTextList[index]
                index += 1
            ind += 1
        try:
            cipherText = ''.join(sum(dec_matrix, []))
        except TypeError:
            raise TypeError("This program cannot",
                            "handle repeating words.")
    
        null_count = cipherText.count('_')
        if null_count > 0:
            return cipherText[: -null_count]
    
        return cipherText
if __name__=="__main__":
    pass
