numbers = []
with open("1_report_repair_input.txt") as f:
    for lines in f.readlines():
        numbers.append(int(lines))

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if (numbers[i] + numbers[j]==2020):
            print(numbers[i]*numbers[j])

# Part Two

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        for k in range(j, len(numbers)):
            if (numbers[i] + numbers[j] + numbers[k]==2020):
                print(numbers[i]*numbers[j]*numbers[k])