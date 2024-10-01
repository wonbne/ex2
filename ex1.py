num1 = float(input("첫 번째 숫자: "))
num2 = float(input("두 번째 숫자: "))
operation = input("+ or - : ")

if operation == '+':
    print(f"결과: {num1 + num2}")
elif operation == '-':
    print(f"결과: {num1 - num2}")
else:
    print("잘못된 연산자입니다.")