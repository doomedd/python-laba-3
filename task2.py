# Введення слова
word = "програмування"

# Використовуємо словник для підрахунку кількості літер
letter_count = {}

# Проходимо через кожну літеру в слові
for letter in word:
    # Якщо літера вже є у словнику, збільшуємо її кількість
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        # Якщо літери ще немає в словнику, додаємо її з кількістю 1
        letter_count[letter] = 1

# Виводимо літери, що повторюються
print("Повторювані літери:")
for letter, count in letter_count.items():
    if count > 1:
        print(letter)