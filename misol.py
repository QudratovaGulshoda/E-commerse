import random

words = ["tiger", "tree", "underground", "giraffe", "chair"]
selected_word = random.choice(words)
print("Keling siz bilan o'yin o'ynaymiz, men bir so'z o'yladm va siz ularni harflarini kiritib so'zni topa olsangiz o'yinda g'olib bo'lasiz agar so'zni topam olmasangiz yutqazasiz. Qani kettik...")
letters = set(selected_word)
wrong_attempts = 0
attempts = 0

while True:
    letter = input("Harfni kiriting: ").lower()
    if letter == "exit":
        break
    attempts += 1
    if letter in letters:
        print(f"To'g'ri! {letter} harfi so'zda bor.")
        letters.remove(letter)
    else:
        print(f"Noto'g'ri.{letter} harfi so'zda yo'q.")
        wrong_attempts += 1
    if not letters:
        print(f"Tabriklayman! Siz so'zni {attempts} urinishda topdingiz.")
        break
    if wrong_attempts >= 5:
        print(
            f"Game over! Siz {wrong_attempts} marta noto'g'ri harf kiritdingiz. To'g'ri javob: {selected_word}.")
        break
