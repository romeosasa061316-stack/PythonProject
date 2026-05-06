# Score Tracker App

players = {}

def add_player():
    name = input("Enter player name: ")
    if name in players:
        print("Player already exists.")
    else:
        players[name] = 0
        print(f"{name} added with 0 points.")

def add_score():
    name = input("Enter player name: ")
    if name not in players:
        print("Player not found.")
        return
    
    try:
        score = int(input("Enter score to add: "))
        players[name] += score
        print(f"{score} points added to {name}.")
    except ValueError:
        print("Invalid score. Enter a number.")

def show_scores():
    if not players:
        print("No players yet.")
        return
    
    print("\n--- Leaderboard ---")
    sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
    
    for name, score in sorted_players:
        print(f"{name}: {score} points")
    print("-------------------\n")

def menu():
    while True:
        print("\nScore Tracker")
        print("1. Add Player")
        print("2. Add Score")
        print("3. Show Leaderboard")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_player()
        elif choice == "2":
            add_score()
        elif choice == "3":
            show_scores()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option. Try again.")

# Run app
menu()