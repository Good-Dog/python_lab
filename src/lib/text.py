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


def tokenize(text: str) -> list[str]:
    words = r"\w+(?:-\w+)*"
    return re.findall(words, text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for i in tokens:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq



def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:n]
