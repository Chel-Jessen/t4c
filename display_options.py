import os
import json

with open("options.json", encoding="utf-8") as f:
    opts = json.load(f)


def display_options(key: str):
    for option in opts[key]:
        print(f"{option}: {opts[key].get(option)}")
    print("")
    choice = input()
    if int(choice) > len(opts[key]) or not choice.isdigit():
        print("Ungültige Eingabe")
        display_options(key)
    return choice


def display_presets(key):
    for option in opts[key]:
        print(f"{option}: {opts[key].get(option)}")
    print("")
    choice = input()
    return choice


def display_validate(options):
    print(options)
    choice = input("Bestätigen (J/N): ").lower()
    if choice == "j":
        return True
    elif choice == "n":
        return False
    else:
        print("Vertippt?")
        display_validate(options)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
