import re
from collections import Counter

STOP_WORDS = {'i', 'a', 'the', 'and', 'to', 'of', 'in', 'is', 'that', 'it', 'for', 'with', 'as', 'on', 'this', 'by',
              'an', 'at', 'from'}

def Analiza(text):
    slowa = re.findall(r'\b\w+\b', text.lower())
    liczba_slow = len(slowa)

    zdania = re.split(r'[.!?]', text)
    liczba_zdan = len([s for s in zdania if s.strip()])

    akapity = text.split('\n\n')
    liczba_akapitow = len([p for p in akapity if p.strip()])

    return liczba_slow, liczba_zdan, liczba_akapitow


def Najczestsze_slowa(text, n=10):
    slowa = re.findall(r'\b\w+\b', text.lower())
    filtrowane_slowa = [word for word in slowa if word not in STOP_WORDS]
    liczba_slow = Counter(filtrowane_slowa)
    return liczba_slow.most_common(n)

def Odwroc_slowa_na_a(text):
    slowa = re.findall(r'\b\w+\b', text)

    def Odwroc_jesli_poczatek_a(slowa):
        if slowa.lower().startswith('a'):
            return slowa[::-1]
        return slowa

    Przemienione_slowa = map(Odwroc_jesli_poczatek_a, slowa)

    Przemieniony_tekst = ' '.join(Przemienione_slowa)
    return Przemieniony_tekst


if __name__ == "__main__":
    Przyklad = """
    Easter Island is an island and special territory of Chile in the southeastern Pacific Ocean, at the southeasternmost 
    point of the Polynesian Triangle in Oceania. The island is renowned for its nearly 1,000 extant monumental 
    statues, called moai, which were created by the early Rapa Nui people. In 1995, UNESCO named Easter Island 
    a World Heritage Site, with much of the island protected within Rapa Nui National Park. \n
    Experts differ on when the island's Polynesian inhabitants first reached the island. While many in the research 
    community cited evidence that they arrived around the year 800, a 2007 study provided compelling evidence 
    suggesting their arrival was closer to 1200.
    """

    liczba_slow, liczba_zdan, liczba_akapitow = Analiza(Przyklad)
    print(f"Liczba słów: {liczba_slow}")
    print(f"Liczba zdań: {liczba_zdan}")
    print(f"Liczba akapitów: {liczba_akapitow}")

    Czeste_slowa = Najczestsze_slowa(Przyklad, 5)
    print("Najczęściej występujące słowa (bez stop words):", Czeste_slowa)

    Przemieniony_tekst = Odwroc_slowa_na_a(Przyklad)
    print("Tekst po transformacji słów zaczynających się na 'a' lub 'A':")
    print(Przemieniony_tekst)
