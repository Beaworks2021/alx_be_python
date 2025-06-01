# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case for priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unknown priority"

# Use if statement to check time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if message.startswith("Reminder:"):
        message += " but it is not time-sensitive."
    else:
        message += ". Consider completing it when you have free time."

# Output the reminder
print(message)
