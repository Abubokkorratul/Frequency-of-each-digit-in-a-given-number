n = input("Enter a number: ")
frequency = {}
for digit in n:
    frequency[digit] = frequency.get(digit, 0) + 1
print("Digit frequencies:")
for digit, freq in frequency.items():
    print(f"{digit}: {freq}")
