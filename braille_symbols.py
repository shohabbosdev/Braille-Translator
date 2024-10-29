import json

class BrailleConverter:
    class Chars:
        chars = "abdefghijklmnopqrstuvxyz"
        db_chars = ["o'", "g'", "sh", "ch"]
        numbers = "1234567890"
        symbols = ',;:.?!"()…-'

    class Braille:
        chars = "⠁⠃⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠽⠗⠎⠞⠥⠺⠹⠯⠵"
        db_chars = "⠧⠻⠱⠟"
        numbers = "⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚"
        symbols = "⠂⠆⠒⠲⠢⠖⠴⠶⠶⠄⠤"
        specific = "⠨⠼⠸⠀"

    def __init__(self, braille_map_path="src/braille_maps.json"):
        with open(braille_map_path, "r") as f:
            self.braille_map = json.load(f)

    def decimal_to_int(self, s):
        return sum(2 ** (6 - int(i)) for i in s)

    def int_to_decimal(self, n):
        binary = bin(n)[2:].zfill(6)
        return "".join(str(i + 1) for i, bit in enumerate(binary) if bit == '1')

    def convert_braille_to_chars(self, braille_symbols):
        """Braille binar belgilarini oddiy matnga o'tkazish."""
        text = ""
        isNum = False

        for binary_char in braille_symbols:
            print(f"Current Braille symbol (6-bit): {binary_char}")  # Har bir 6-bitlik belgini tekshirish uchun

            # Bo'sh joy belgisiga mos keladigan binar kodni tekshirish
            if binary_char == "000000":  
                text += " "
                isNum = False
                continue

            # Raqamlar boshlanish belgisini tekshirish
            if binary_char == "001111":  
                isNum = True
                continue

            # Raqamlar uchun mos keladigan qiymatni tekshirish
            if isNum and binary_char in self.Braille.numbers:
                text += str(self.Braille.numbers.index(binary_char) + 1)
                continue

            # Harf belgilarini qidirish
            if binary_char in self.Braille.chars:
                text += self.Chars.chars[self.Braille.chars.index(binary_char)]
                isNum = False
                continue

            # Qo'sh harflar uchun tekshiruv
            if binary_char in self.Braille.db_chars:
                text += self.Chars.db_chars[self.Braille.db_chars.index(binary_char)]
                continue

        print(f"Final translated text: {text}")  # Tarjima qilingan matnni tekshirish
        return text

    def convert_chars_to_braille(self, text):
        braille_str = ""
        isNum = False

        for i, char in enumerate(text):
            if char == " ":
                braille_str += self.Braille.specific[3]  # Brailledagi bo'sh joy belgisi
                isNum = False
                continue

            if char in self.Chars.symbols:
                symbol_index = self.Chars.symbols.index(char)
                braille_str += self.Braille.symbols[symbol_index]
                continue

            if char.isdigit():
                if not isNum:
                    braille_str += self.Braille.specific[1]  # Raqamlar oldidagi maxsus belgi
                    isNum = True
                braille_str += self.Braille.numbers[int(char) - 1]
                continue

            char_lower = char.lower()
            if char_lower in self.Chars.chars:
                if char.isupper():
                    braille_str += self.Braille.specific[0]  # Katta harflar uchun belgi
                braille_str += self.Braille.chars[self.Chars.chars.index(char_lower)]
                continue

            if i < len(text) - 1:
                double_char = text[i:i+2].lower()
                if double_char in self.Chars.db_chars:
                    braille_str += self.Braille.db_chars[self.Chars.db_chars.index(double_char)]
                    text = text[:i] + text[i+2:]  # Qo'sh harflar uchun textni yangilash
                    continue

        return braille_str

    def convert_braille_to_binary(self, s):
        return [list(map(int, bin(ord(i) - 10240)[2:].zfill(6)[::-1])) for i in s]

    def convert_braille_to_digits(self, s):
        binary = self.convert_braille_to_binary(s)
        return ["".join(str(i + 1) for i, bit in enumerate(bits) if bit) for bits in binary]

    def convert_char_to_binary(self, s):
        return self.convert_braille_to_binary(self.convert_chars_to_braille(s))

    def viewer(self, s, t="binary"):
        if t == "binary":
            return [f"{b[0]}{b[3]}\n{b[1]}{b[4]}\n{b[2]}{b[5]}\n\n" for b in s]

# Foydalanish
# converter = BrailleConverter()

# # Matnni Braille kodiga o'zgartirish
# text = "Salom!"
# braille_code = converter.convert_chars_to_braille(text)
# print("Braille kiritilgan matn:", braille_code)

# # Braille kodini matnga o'zgartirish
# braille_symbols = ["100000", "110000", "010100", "011000"]  # Masalan, 'Salom'
# converted_text = converter.convert_braille_to_chars(braille_symbols)
# print("Braille belgilaridan matnga:", converted_text)

# # Braille kodini ikkilik ko'rinishga aylantirish
# binary = converter.convert_braille_to_binary(braille_code)
# print("Braille ikkilik shaklda:", binary)
