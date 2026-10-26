"""Project Two starter for the student's text-based adventure game."""

Created by: Serena Paulson


def show_instructions():
    """Display the game objective and available commands."""
    print("Welcome to Operation Shadow Signal!")
    print("Collect all 6 items before confronting SHADOW.")
    print("Move commands: go North, go South, go East, go West")
    print("Collect items: get Item Name")
    print("Exit game: exit").
    pass


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("---------------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        item = rooms[current_room]["item"]

        if item not in inventory:
            print("You see a", item)

    print("---------------------------")
    pass



def main():
    """Run the main gameplay loop."""

    # Dictionary of rooms, directions, and items
    rooms = {
        "Entry Hall": {
            "north": "Communications Center",
            "east": "Equipment Storage"
        },
        "Communications Center": {
            "south": "Entry Hall",
            "east": "Intelligence Office",
            "item": "Encryption Key"
        },
        "Equipment Storage": {
            "west": "Entry Hall",
            "north": "Intelligence Office",
            "south": "Power Station",
            "item": "Tactical Radio"
        },
        "Intelligence Office": {
            "west": "Communications Center",
            "south": "Equipment Storage",
            "east": "Cyber Operations Room",
            "item": "Classified Intel"
        },
        "Cyber Operations Room": {
            "west": "Intelligence Office",
            "south": "Security Office",
            "item": "Access Card"
        },
        "Power Station": {
            "north": "Equipment Storage",
            "east": "Security Office",
            "item": "Power Cell"
        },
        "Security Office": {
            "west": "Power Station",
            "north": "Cyber Operations Room",
            "east": "Central Control Room",
            "item": "Override Code"
        },
        "Central Control Room": {
            "west": "Security Office"
        }
    }

    # Starting room and inventory
    current_room = "Entry Hall"
    inventory = []

    # Display instructions
    show_instructions()

    # Main gameplay loop
    while True:
        show_status(current_room, inventory, rooms)

        # Check if player encounters the villain
        if current_room == "Central Control Room":
            if len(inventory) == 6:
                print("Congratulations!")
                print("You collected all 6 items and defeated SHADOW!")
                print("You have restored control of the facility!")
            else:
                print("SHADOW has detected your presence!")
                print("You entered without all 6 items.")
                print("Game Over!")
            break

        # Get player's command
        command = input("Enter your move: ").strip()
        command_lower = command.lower()

        # Exit command
        if command_lower == "exit":
            print("Thanks for playing!")
            break

        # Movement commands
        elif command_lower.startswith("go "):
            direction = command_lower[3:].strip()

            if direction in rooms[current_room]:
                if direction != "item":
                    current_room = rooms[current_room][direction]
                else:
                    print("Invalid direction!")
            else:
                print("You cannot go that way!")

        # Get item commands
        elif command_lower.startswith("get "):
            requested_item = command[4:].strip()

            if "item" in rooms[current_room]:
                room_item = rooms[current_room]["item"]

                if requested_item.lower() == room_item.lower():
                    inventory.append(room_item)
                    print(f"You collected the {room_item}!")
                    del rooms[current_room]["item"]
                else:
                    print("That item is not in this room!")
            else:
                print("There is no item to collect here!")

        # Invalid commands
        else:
            print("Invalid command! Use 'go direction' or 'get item'.")
    pass


if __name__ == "__main__":
    main()
