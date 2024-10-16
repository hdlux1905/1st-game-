import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 50

    def choose_force(self):
        while True:
            try:
                force = int(input(f"{self.name}, choose your attack force (1-9): "))
                if 1 <= force <= 9:
                    return force
                else:
                    print("Force must be between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

    def hit_success(self, force):
        success_rate = max(0, 100 - (force - 1) * 10)  # Calculate success rate
        return random.randint(1, 100) <= success_rate

def attack(attacker, defender):
    force = attacker.choose_force()
    if attacker.hit_success(force):
        defender.hp -= force
        print(f"{attacker.name} hits {defender.name} for {force} damage!")
    else:
        print(f"{attacker.name}'s attack missed!")

def human_vs_human():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    while player1.hp > 0 and player2.hp > 0:
        attack(player1, player2)
        if player2.hp <= 0:
            print(f"{player2.name} has been defeated! {player1.name} wins!")
            break
        attack(player2, player1)
        if player1.hp <= 0:
            print(f"{player1.name} has been defeated! {player2.name} wins!")

def human_vs_dummy():
    player = Player("Human Player")
    computer = Player("Dummy Computer")

    while player.hp > 0 and computer.hp > 0:
        attack(player, computer)
        if computer.hp <= 0:
            print(f"{computer.name} has been defeated! {player.name} wins!")
            break
        
        force = random.randint(1, 9)
        print(f"{computer.name} chooses a random force: {force}")
        if computer.hit_success(force):
            player.hp -= force
            print(f"{computer.name} hits {player.name} for {force} damage!")
        else:
            print(f"{computer.name}'s attack missed!")

def human_vs_smart():
    player = Player("Human Player")
    computer = Player("Smart Computer")

    while player.hp > 0 and computer.hp > 0:
        attack(player, computer)
        if computer.hp <= 0:
            print(f"{computer.name} has been defeated! {player.name} wins!")
            break
        
        # Smart strategy for the computer
        if computer.hp > player.hp:
            force = random.randint(5, 9)  # Higher force when ahead
        else:
            force = random.randint(1, 5)   # Lower force when behind
        print(f"{computer.name} chooses a strategic force: {force}")
        
        if computer.hit_success(force):
            player.hp -= force
            print(f"{computer.name} hits {player.name} for {force} damage!")
        else:
            print(f"{computer.name}'s attack missed!")

def main():
    print("Welcome to the Text Fighting Game!")
    while True:
        print("\nChoose a game configuration:")
        print("1. Human vs. Human")
        print("2. Human vs. Dummy Computer")
        print("3. Human vs. Smart Computer")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            human_vs_human()
        elif choice == '2':
            human_vs_dummy()
        elif choice == '3':
            human_vs_smart()
        else:
            print("Invalid choice. Please select again.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
