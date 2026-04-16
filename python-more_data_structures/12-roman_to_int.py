#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    roman_string = roman_string.upper().strip()

    if any(ch not in roman_dict for ch in roman_string):
        raise ValueError(f"Geçersiz Roman rakamı: '{roman_string}'")

    num = 0
    prev_val = 0

    for ch in reversed(roman_string):
        val = roman_dict[ch]
        if val < prev_val:
            num -= val
        else:
            num += val
        prev_val = val

    return num


if __name__ == "__main__":
    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("", 0),
        (None, 0),
    ]

    for roman, expected in test_cases:
        result = roman_to_int(roman)
        status = "✓" if result == expected else "✗"
        print(f"{status} roman_to_int('{roman}') = {result} (beklenen: {expected})")
