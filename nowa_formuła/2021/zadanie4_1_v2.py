with open("instrukcje.txt", "r") as file:
    instructions = []
    for line in file:
        instructions.append(line.strip().split()[0])

# Wystarczy, że policzymy ile jest instrukcji DOPISZ i odejmiemy od tego ilość instrukcji USUN
length = instructions.count("DOPISZ") - instructions.count("USUN")

print(length)

with open("wyniki4.txt", "w", encoding='UTF-8') as out:
    out.write("4.1\n")
    out.write(str(length) + "\n")