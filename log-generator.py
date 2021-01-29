days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def print_logs():
    n = 0
    for day in days_of_week:
        # if date <= 28:
        weekday = days_of_week[n]
        count = 33 + n
        date = 8 + n
        n += 1
        print(f'### Day {count}: {weekday}, February {date}, 2021')
        print()
        print('**Today\'s Progress**:')
        print()
        print('**Link(s) to work**')
        print('1. [GitHub](https://github.com/yvonneyeh)')
        print()
        print()
        print()

print_logs()
