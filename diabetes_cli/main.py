import sys
from logger import log_blood_sugar, log_insulin
from stats import show_stats
from graph import plot_graph

def run_menu():
    while True:
        # Display the menu
        print("\n🩺 Welcome to the Diabetes Tracker CLI\n")
        print("1. Log blood sugar")
        print("2. Log insulin")
        print("3. View stats")
        print("4. View blood sugar graph")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

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
            log_blood_sugar(value, time, note) # Log the blood sugar value

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
            log_insulin(kind, amount, time, note) # Log the insulin dose 

        elif choice == "3":
            show_stats()

        elif choice == "4":
            plot_graph("blood_sugar")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

def parse_cli_args(args):
    if not args or args[0] in ("--help", "help"):
        print("Usage:")
        print("  blood-sugar --value <float> --time <HH:MM> [--note <text>]")
        print("    Log a blood sugar value. Example:")
        print("    python main.py blood-sugar --value 120 --time 08:30 --note \"Fasting\"")
        print()
        print("  insulin --kind <bolus|basal> --amount <float> --time <HH:MM> [--note <text>]")
        print("    Log an insulin dose. Example:")
        print("    python main.py insulin --kind bolus --amount 5 --time 12:00 --note \"Lunch\"")
        print()
        print("  stats")
        print("    Show all logged data in a table.")
        print()
        print("  graph --type <blood_sugar|insulin>")
        print("    Show a graph for the selected type. Example:")
        print("    python main.py graph --type blood_sugar")
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
        elif command == "stats":
            show_stats()
        elif command == "graph":
            if "--type" not in args:
                print("Missing --type argument for graph.")
                return
            graph_type = args[args.index("--type") + 1]
            plot_graph(graph_type)
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