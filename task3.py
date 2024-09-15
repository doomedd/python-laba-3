# Введення речення
sentence = "Наука не стоїть на місці, навпаки, вона постійно розвивається."

# Розбиваємо речення на слова
words = sentence.split()

# Лічильник слів, що починаються з літери "н"
count = 0

# Перевіряємо кожне слово
for word in words:
    # Якщо слово починається з літери "н"
    if word.lower().startswith('н'):
        count += 1

# Виводимо результат
print("Кількість слів, що починаються з літери 'н':", count)