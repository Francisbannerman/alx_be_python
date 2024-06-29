# daily_reminder.py

while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    match priority:
        case 'high':
            if time_bound == 'yes':
                reminder = " that requires immediate attention today!"
            else:
                reminder = " . Consider completing it when you have free time."
        case 'medium':
            if time_bound == 'yes':
                reminder = " that requires immediate attention today!"
            else:
                reminder = " . Consider completing it when you have free time."
        case 'low':
            if time_bound == 'yes':
                reminder = " that requires immediate attention today!"
            else:
                reminder = " . Consider completing it when you have free time."
        case _:
            reminder = "Invalid priority entered. Please use high, medium, or low."
    
    print(task, " is a ", priority, " priority task", reminder)
