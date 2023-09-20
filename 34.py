def check_rhythm(poem):
    lines = poem.split() 
    syllables_count = None 

    for line in lines:
        words = line.split('-')  # Разделяем фразу на слова

        current_syllables_count = sum(1 for word in words for letter in word if letter.lower() in 'aeiouаеёиоуыэюя')

        if syllables_count is None:
            syllables_count = current_syllables_count
        elif syllables_count != current_syllables_count:
            return "Пам парам" 

    return "Парам пам-пам"  

poem_input = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem_input)
print(result)