# ta funkcja zwraca słownik, który w kluczach malitery, a w wartościach liczbę ich wystąpień w liście
def num_of_occuraces(list):
    occurances = dict()
    for letter in list:
        occurances.update({letter: list.count(letter)})

    return occurances

# ta funkcja zwraca literę, która jest dopisywana najczęściej i liczbę jej wystąpień
def get_dominant_letter(dict):
    max_num_of_occurances = max(dict.values())

    for letter in dict:
        if dict[letter] == max_num_of_occurances:
            return letter, max_num_of_occurances

with open("instrukcje.txt", "r") as file:
    instructions = []
    for line in file:
        if line.strip().split()[0] == "DOPISZ":
            instructions.append(line.strip().split()[1])

# wywołujemy wszyskie potrzebne funkcje, aby otrzymać literę (dominantę) i ilość jej wystąpień
dominant_letter = get_dominant_letter(num_of_occuraces(instructions))
print(f"{dominant_letter[0]} {dominant_letter[1]}")

with open("wyniki4.txt", "a", encoding='UTF-8') as out:
    out.write("\n4.2\n")
    out.write(f"{dominant_letter[0]} {dominant_letter[1]}\n\n")