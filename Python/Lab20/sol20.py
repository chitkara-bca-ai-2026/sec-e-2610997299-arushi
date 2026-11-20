import os

def append_entry(filename, entry):
    with open(filename, 'a') as file:
        file.write(entry + '\n')

def display_log(filename):
    if not os.path.exists(filename):
        print(f"\n--- {filename} does not exist yet. Add an entry first! ---")
        return

    print("\n--- Daily Log Entries ---")
    with open(filename, 'r') as file:
        entries = file.readlines()
        
    if not entries:
        print("The log file is empty.")
    else:
        for idx, line in enumerate(entries, start=1):
            print(f"{idx}. {line.strip()}")
    print("-------------------------\n")

def pre_populate_file(filename):
    if not os.path.exists(filename):
        sample_entries = [
            "09:00 AM - Office opened and systems checked.",
            "11:30 AM - Morning team sync completed.",
            "03:15 PM - Server maintenance scheduled."
        ]
        with open(filename, 'w') as file:
            for entry in sample_entries:
                file.write(entry + '\n')

def main():
    filename = "./python/Lab20/daily_log.txt"
    pre_populate_file(filename)
    
    while True:
        print("=== Daily Log Book Menu ===")
        print("1. Add Log Entry")
        print("2. Display Complete Log")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            log_input = input("Enter a log message (e.g., timestamped activity): ").strip()
            if log_input:
                append_entry(filename, log_input)
                print("Log entry successfully added.\n")
            else:
                print("Log entry cannot be empty.\n")
                
        elif choice == '2':
            display_log(filename)
            
        elif choice == '3':
            print("Thank you for using Daily Log Book. Goodbye!")
            break
            
        else:
            print("Invalid selection. Please choose a valid option (1 to 3).\n")

if __name__ == "__main__":
    main()