"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"}
}

# Set the player's starting room.
current_room = "Great Hall"

# Create the gameplay loop.
while True:
    # Display the current room.
    print(f"You are in the {current_room}")

    # Prompt the player for a command.
    command = input("Enter a direction (north, south, east, west) or exit: ").lower().strip()

    # Check if the player wants to exit.
    if command == "exit":
        print("Thanks for playing!")
        break

    # Check if the direction is valid.
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]

    # Handle invalid directions.
    else:
        print("Invalid direction. Try again.")
