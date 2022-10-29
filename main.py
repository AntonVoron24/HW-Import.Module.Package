import application.salary as salary
import application.db.people as people
from datetime import datetime as dt
import snoop


@snoop
def factorial(x: int):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


if __name__ == '__main__':
    print(f"Дата: {dt.now().strftime('%d.%m.%Y')}")
    print(f"Время: {dt.now().strftime('%H:%M')}")
    salary.calculate_salary()
    people.get_employees()

    print("*" * 30)
    num = 5
    print(f"The factorial of {num} is {factorial(num)}")
