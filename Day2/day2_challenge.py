question_one = input("What is your name?")
question_two = input("How much did you sale?")

question_two = int(question_two)
employee_commission = question_two * 13 / 100

print(question_one)
print(question_two)
print(f"Your commission is {employee_commission}")