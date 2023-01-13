ranking = {1: "Elden Ring", 2: "Borderlands 2", 3: "Call of Duty Modern Warfare 2", 4: "Tiny Tina Wonderlands",
           5: "Cyberpunk 2077", 6: "Borderlands 3", 7: "Resident Evil 3 Nemesis", 8: "Divinity Original Sin 2",
           9: "Terraria", 10: "League Of Legends"}

while True:
    position = int(input("What position you want to know?: "))
    if position == 0:
        break
    elif position in ranking:
        print("The Number", position, "is", ranking[position])
    else:
        print("Invalid Position, please type a valid position.")
