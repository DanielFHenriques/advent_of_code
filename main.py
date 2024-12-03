import twenty_four

lookup = {
    2024: twenty_four.lookup
}

if __name__ == '__main__':
    print('Welcome to the Advent of Code')

    print('Choose the year:', end=' ')
    year = int(input())

    print('Choose the day:', end=' ')
    day = int(input())

    exercise = lookup[year][day]
    exercise.solve()
