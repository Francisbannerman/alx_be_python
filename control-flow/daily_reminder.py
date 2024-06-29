# daily_reminder.py

while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    reminder = f"'{task}' is a {priority} priority task."
    
    match priority:
        case 'high':
            if time_bound == 'yes':
                reminder += " It requires immediate attention today!"
            else:
                reminder += " Make sure to prioritize it today."
        case 'medium':
            if time_bound == 'yes':
                reminder += " Try to complete it by the end of the day."
            else:
                reminder += " Plan to complete it within the next few days."
        case 'low':
            if time_bound == 'yes':
                reminder += " Aim to finish it soon."
            else:
                reminder += " Consider completing it when you have free time."
        case _:
            reminder = "Invalid priority entered. Please use high, medium, or low."
    
    print("\nReminder:", reminder)
    
    another = input("Would you like to enter another task? (yes/no): ").lower()
    if another != 'yes':
        break
