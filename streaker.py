import datetime
import json

def add_entry():
    today = datetime.date.today()
    entry = input("Enter your contribution for today: ")

    # Load existing entries from file
    try:
        with open('streak.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Add today's entry
    data.append({"date": str(today), "entry": entry})

    # Save updated entries to file
    with open('streak.json', 'w') as file:
        json.dump(data, file)

    print("Entry added successfully!")

def display_streak():
    try:
        with open('streak.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    streak = len(data)
    print("Current streak: {} days".format(streak))

    for entry in data:
        print("{}: {}".format(entry['date'], entry['entry']))

# Main program loop
while True:
    print("\nStreak Tracker")
    print("1. Add entry")
    print("2. Display streak")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_entry()
    elif choice == '2':
        display_streak()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

print("Exiting Streak Tracker.")