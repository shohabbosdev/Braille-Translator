import unicodedata
import json
import re
from latin_cyrillic_symbols import to_cyrillic

# JSON fayllarini o'qing
with open("models/uz-cyril.json", "r", encoding="utf-8") as f:
    uz_cyril = json.load(f)

with open("models/uz-latin.json", "r", encoding="utf-8") as f:
    uz_latin = json.load(f)

i18n = {"uzCyril": uz_cyril, "uzLatin": uz_latin}

written_number = {"lang": "uzLatin"}

number_to_words_uz = {}


def number_to_scales_uz(num):
    try:
        number = str(num)
        is_minus_exists = False
        if check_if_exists_minus(number):
            is_minus_exists = True
            number = number.replace("-", "")

        number_length = len(number)
        number_scales = (number_length + 2) // 3
        number_length_goal = number_scales * 3
        lack_of_digits = number_length_goal - number_length
        extended_number = "0" * lack_of_digits + number

        cut_number = []
        if is_minus_exists:
            cut_number.append("-")

        for i in range(0, len(extended_number), 3):
            digit1 = extended_number[i]
            digit2 = extended_number[i + 1] if i + 1 < len(extended_number) else "0"
            digit3 = extended_number[i + 2] if i + 2 < len(extended_number) else "0"
            digits = digit3 + digit2 + digit1
            cut_number.append(digits)

        return cut_number[::-1]
    except Exception as e:
        print("Xatolik number_to_scales_uz funksiyasida sodir bo'ldi matni: %s" % e)
        return None

def check_if_exists_minus(number):
    try:
        return number[0] == "-"
    except Exception as e:
        print("Xatolik check_if_exists_minus funksiyasida sodir bo'ldi matni: %s" % e)
        return None

def convert_scales_to_words_uz(number_arr, options=None):
    try:
        if not options:
            options = written_number

        lang_id = options["lang"] if isinstance(options["lang"], str) else options["lang"]

        if not lang_id:
            if written_number["lang"] not in i18n:
                written_number["lang"] = "uzLatin"
            lang_id = i18n[written_number["lang"]]
        else:
            lang_id = i18n[lang_id]

        converted_result = ""
        is_minus = False

        if number_arr[-1] == "-":
            is_minus = True
            number_arr = number_arr[:-1]

        for index, element in enumerate(number_arr):
            digit1 = int(element[0])
            digit2 = int(element[1])
            digit3 = int(element[2])
            unit_name = lang_id["units"][index]

            hundred_unit_name = ""
            digit1_text = ""
            digit2_text = ""
            digit3_text = ""

            if digit1 == 0 and digit2 == 0 and digit3 == 0:
                continue

            digit1_text = lang_id["numberNames"][0][digit1]
            digit2_text = lang_id["numberNames"][1][digit2]

            if digit3 != 0:
                hundred_unit_name = lang_id["numberNames"][2][2]

            digit3_text = lang_id["numberNames"][0][digit3]

            is_unit_name = index != 0 and not (digit1 == 0 and digit2 == 0 and digit3 == 0)

            scale_result = f"{digit3_text} {hundred_unit_name} {digit2_text} {digit1_text} {unit_name if is_unit_name else ''}"
            scale_result = " ".join(scale_result.split())

            converted_result = f"{scale_result} {converted_result}"

        if is_minus:
            converted_result = f"{lang_id['minus']} {converted_result}"

        return converted_result.strip()
    except Exception as e:
        print("Xatolik convert_scales_to_words_uz funksiyasida sodir bo'ldi matni: %s" % e)
        return None

def number_to_words_uz_convert(number, options=None):
    try:
        if number == 0:
            return "No'l"
        elif number == "NoneType":
            print("Son kiritish maydoni bo'sh bo'lmasligi kerak!!!")
            raise None
        elif number >= 1:
            number = str(number)
            before_dot = number
            after_dot = None

            if "." in number:
                before_dot, after_dot = number.split(".")
            elif "," in number:
                before_dot, after_dot = number.split(",")

            converted_result = ""


            before_dots = number_to_scales_uz(before_dot)
            before_dot_convert = convert_scales_to_words_uz(before_dots, options)
            converted_result = before_dot_convert.strip()

            if after_dot is not None:
                after_dots = number_to_scales_uz(after_dot)
                after_dot_convert = convert_scales_to_words_uz(after_dots, options)
                lang_id = (
                    i18n[options["lang"]] if options else i18n[written_number["lang"]]
                )
                converted_result = (
                    f"{converted_result} {lang_id['point']} {after_dot_convert.strip()}"
                )
            return converted_result.capitalize()
        else:
            print("Siz manfiy yoki noto'g'ri qiymat kiritdingiz")
            return None
    except Exception as e:
        print("Xatolik sodir bo'ldi xatolik ifodasi: %s" % e)
        return None

REPLACE_DICT = {
    "\n": " ",  # Yangi qator belgisi
    """: " ",  # Qo'shtirnoq belgisi
    """: " ",  # Qo'shtirnoq belgisi
    "«": " ",  # Qo'shtirnoq belgisi
    "»": " ",  # Qo'shtirnoq belgisi
    "—": " ",  # Defis belgisi
    "+": " ",  # Qo'shish belgisi
    "_": " ",  # Pastki chiziq belgisi
    "!": " ",  # Undov belgisi
    "@": " ",  # Kuchukcha belgisi
    "#": " ",  # Panjara belgisi
    "$": " ",  # Dollar belgisi
    "%": " ",  # Foiz belgisi
    "^": " ",  # Daraja belgisi
    "&": " ",  # Va belgisi
    "*": " ",  # Yulduzcha belgisi
    "(": " ",  # Ochiluvchi Qavs
    ")": " ",  # Yopiluvchi Qavs
    "-": " ",  # Defis belgisi
    "=": " ",  # Tenglik belgisi
    "{": " ",  # Ochiluvchi jingalak Qavs
    "}": " ",  # Yopiluvchi jingalak Qavs
    "[": " ",  # Ochiluvchi kvadrat Qavs
    "]": " ",  # Yopiluvchi kvadrat Qavs
    "|": " ",  # Vertikal chiziq belgisi
    ";": " ",  # Nuqta-vergul belgisi
    ":": " ",  # Ikki nuqta belgisi
    "`": " ",  # Escni tagidagi belgi
    "<": " ",  # Kichik belgisi
    ">": " ",  # Katta belgisi
    ",": " ",  # Vergul
    ".": " ",  # Nuqta
    "/": " ",  # Slash
    "?": " ",  # So'roq belgisi
}

def replace_numbers(text):
    try:
        # Raqamdan keyin kelgan '-' belgisini 'inchi' deb yozamiz
        text = re.sub(r"(\d+)-", lambda x: number_to_words_uz_convert(int(x.group(1))) + "inchi", text)
        # Raqamdan keyin kelgan '%' belgisini 'foiz' deb yozamiz
        text = re.sub(r"(\d+)%", lambda x: number_to_words_uz_convert(int(x.group(1))) + "foiz", text)
        # Raqamdan keyin kelgan '.' belgisini 'butun' deb yozamiz
        # text = re.sub(r"(\d+).", lambda x: number_to_words_uz_convert(int(x.group(1))) + "butun", text)
        # Sonlarni so'zga konvertatsiya qilamiz
        text = re.sub(r"\b\d+\b", lambda x: number_to_words_uz_convert(int(x.group())), text)
        # print("Matnda kerakli almashtirishlar bajarildi!!!")
        return text
    except Exception as e:
        return f"🌐Almashtirishda xatolik bor: {e}"

def detect_script(text):
    for char in text:
        try:
            if unicodedata.name(char).startswith("LATIN"):
                return "Latin"
            else:
                return "Krill"
        except ValueError:
            raise ValueError("Invalid")

def clean_text_number(text):
    try:
        if text!='':
            text = replace_numbers(text)
            text = "".join([REPLACE_DICT.get(i, i) for i in text])
            text = to_cyrillic(text) if detect_script(text) == "Latin" else text
            return text
        else:
            print("Bo'sh maydon bo'lmasligiga e'tibor bering!!!")
            return None
    except Exception as e:
        print("🌐Clean Text funksiyasida xatolik bor") 
        return None 


# print(clean_text_number("Assalomu alaykum 15 ga kelaman"))