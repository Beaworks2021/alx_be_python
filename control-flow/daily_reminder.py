# daily_reminder.py
# Personal Daily Reminder Script
# Uses conditional statements, Match Case, and loops for task reminders

def main():
    print("=== Daily Task Reminder ===")
    
    # Prompt for a single task
    task = input("Enter your task: ").strip()
    
    # Get priority level with validation loop
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Please enter 'high', 'medium', or 'low'")
    
    # Get time sensitivity with validation loop
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ['yes', 'no']:
            break
        else:
            print("Please enter 'yes' or 'no'")
    
    # Process the task using Match Case for priority
    match priority:
        case 'high':
            if time_bound == 'yes':
                print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"\nReminder: '{task}' is a high priority task. Make sure to complete it today!")
        
        case 'medium':
            if time_bound == 'yes':
                print(f"\nReminder: '{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"\nNote: '{task}' is a medium priority task. Try to complete it soon.")
        
        case 'low':
            if time_bound == 'yes':
                print(f"\nReminder: '{task}' is a low priority task that requires immediate attention today!")
            else:
                print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    
    # Optional: Ask if user wants to set another reminder
    while True:
        another = input("\nWould you like to set another reminder? (yes/no): ").strip().lower()
        if another in ['yes', 'no']:
            break
        else:
            print("Please enter 'yes' or 'no'")
    
    if another == 'yes':
        print("\n" + "="*30)
        main()  # Recursive call to restart the process
    else:
        print("\nHave a productive day!")

# Run the program
if __name__ == "__main__":
    main()