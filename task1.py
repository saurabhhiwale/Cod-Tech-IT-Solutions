def main():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself standing at a crossroad.")

    while True:
        print("\nWhat do you want to do?")
        print("1. Go left")
        print("2. Go right")
        print("3. Stay put")

        choice = input("Enter your choice (1/2/3): ").strip()  # Add .strip() to remove leading/trailing whitespace

        if choice == '1':
            print("You chose to go left.")
            print("You encounter a dragon!")
            print("Game over!")
            break
        elif choice == '2':
            print("You chose to go right.")
            print("You find a treasure chest!")
            print("Congratulations, you win!")
            break
        elif choice == '3':
            print("You chose to stay put.")
            print("Nothing happens.")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
