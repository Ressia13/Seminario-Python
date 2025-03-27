

def is_anagram(word1, word2):

    if len(word1) == len(word2):

        for letter in word1.strip():

            if letter not in word2.strip():
                return False
        return True
    else:return False


word1 = input("ingrese una palabra: ").strip()
word2 = input("Ingrese otra palabra: ").strip()
if is_anagram(word1, word2):
    print(f"{word1} y {word2} son anagramas.")
else:
    print("No son anagramas.")
