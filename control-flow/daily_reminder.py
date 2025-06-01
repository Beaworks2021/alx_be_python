# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process and print reminder using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unknown priority"

# Modify reminder if time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if "Note" in message:
        message += ". Consider completing it when you have free time."
    else:
        message += " but it is not time-sensitive."

# Output the customized reminder
print("\n" + message)
