# AI log: none
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
week = {i + 1: j for i, j in enumerate(days)}
print(week)
reverse_week = {j: i for i, j in week.items()}
print(reverse_week)

# Очікую значення days[0] = 'Monday', week[1] = 'Monday' та reverse_week["Sunday"] = 7