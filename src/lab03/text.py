import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    text = " ".join(text.split())

    return text
print('normalize')
print(r'"ПрИвЕт\nМИр\t" ->', normalize("ПрИвЕт\nМИр\t"))
print('"ёжик, Ёлка"" ->', normalize("ёжик, Ёлка"))
print(r'"Hello\r\nWorld"" ->', normalize("Hello\r\nWorld"))
print('"  двойные   пробелы  "" ->', normalize("  двойные   пробелы  "))

def tokenize(text: str) -> list[str]:
    words = r"\w+(?:-\w+)*"
    return re.findall(words, text)
print('')
print('tokenize')
print('"привет мир" ->', tokenize("привет мир"))
print('"hello,world!!!" ->', tokenize("hello,world!!!"))
print('"по-настоящему круто" ->', tokenize("по-настоящему круто"))
print('"2025 год" ->', tokenize("2025 год"))
print('"emoji 😀 не слово" ->', tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for i in tokens:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
print('')
print('count_freq')
print('["a","b","a","c","b","a"] ->', count_freq(["a","b","a","c","b","a"]))
print('["bb","aa","bb","aa","cc"] ->', count_freq(["bb","aa","bb","aa","cc"]))
freq1 = count_freq(["a","b","a","c","b","a"])
freq2 = count_freq(["bb","aa","bb","aa","cc"])
print('')

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:n]
print('top_n')
print(freq1, '->', top_n(freq1, n=2))
print(freq2, '->', top_n(freq2, n=2))