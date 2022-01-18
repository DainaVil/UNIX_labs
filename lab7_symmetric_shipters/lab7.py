DICT = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцшщъыьэюя .,;?:!()-|\"«»'"

class Encrypt:
    def __init__(self, key, string):

        out = ""
        for char in string:
            out += self.encrypt(char, key)
        self.encrypted = out

        st = ""
        for char in out:
            st += self.decrypt(char, key)
        self.decrypted = st

    def encrypt(self, char, key):
        st = DICT
        index = st.find(char)

        if key > len(st):
            key = key - len(st)

        if index + key >= len(st):
            return st[index + key - len(st)]
        else:
            return st[index + key]

    def decrypt(self, char, key):
        st = DICT
        index = st.find(char)

        if key > len(st):
            key = key - len(st)

        if index - key >= len(st):
            return st[index - key + len(st)]
        else:
            return st[index - key]


def main():
    try:
        key = int(input("Key: "))
        st = str(input("String to encrypt: "))
    except:
        print("Error")
        return

    obj = Encrypt(key, st)
    print("Encrypted: " + obj.encrypted)
    print("Decrypted: " + obj.decrypted)

if __name__ == "__main__":
    main()
