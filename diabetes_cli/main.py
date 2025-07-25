import sys
from logger import log_blood_sugar, log_insulin

def run_menu():
    while True:
        print("\n🩺 Welcome to the Diabetes Tracker CLI\n")
        print("1. Log blood sugar")
        print("2. Log insulin")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            try:
                value = float(input("Enter blood sugar value (mg/dL): "))
                if value <= 0:
                    print("Value must be positive.")
                    continue
            except ValueError:
                print("Invalid number entered.")
                continue
            time = input("Enter time (HH:MM): ")
            note = input("Enter a note (optional): ")
            log_blood_sugar(value, time, note)

        elif choice == "2":
            kind = input("Enter insulin type (bolus/basal): ")
            try:
                amount = float(input("Enter insulin amount (units): "))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
            except ValueError:
                print("Invalid number entered.")
                continue
            time = input("Enter time (HH:MM): ")
            note = input("Enter a note (optional): ")
            log_insulin(kind, amount, time, note)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

def parse_cli_args(args):
    if not args or args[0] in ("--help", "help"):
        print("Usage:")
        print("  blood-sugar --value <float> --time <HH:MM> [--note <text>]")
        print("  insulin --kind <bolus|basal> --amount <float> --time <HH:MM> [--note <text>]")
        return
    command = args[0]
    try:
        if command == "blood-sugar":
            if "--value" not in args or "--time" not in args:
                print("Missing --value or --time argument.")
                return
            value = float(args[args.index("--value") + 1])
            time = args[args.index("--time") + 1]
            note = ""
            if "--note" in args:
                note = args[args.index("--note") + 1]
            log_blood_sugar(value, time, note)
        elif command == "insulin":
            if "--kind" not in args or "--amount" not in args or "--time" not in args:
                print("Missing --kind, --amount, or --time argument.")
                return
            kind = args[args.index("--kind") + 1]
            amount = float(args[args.index("--amount") + 1])
            time = args[args.index("--time") + 1]
            note = ""
            if "--note" in args:
                note = args[args.index("--note") + 1]
            log_insulin(kind, amount, time, note)
        else:
            print("Unknown command. Run with no arguments for the interactive menu.")
    except (ValueError, IndexError):
        print("Invalid arguments provided.")

def main():
    if len(sys.argv) > 1:
        parse_cli_args(sys.argv[1:])
    else:
        run_menu()

if __name__ == "__main__":
    main()