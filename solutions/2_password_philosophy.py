policy_limits, policy_char, password = [], [], []

with open("2_password_philosophy_input.txt") as f:
    for lines in f.readlines():
        fields = lines.split(" ")
        policy_limits.append(fields[0])
        policy_char.append(fields[1])
        password.append(fields[2])
        
sum = 0
for i in range(len(password)):
    low_limit = int(policy_limits[i].split("-")[0])
    high_limit = int(policy_limits[i].split("-")[1])
    letter = policy_char[i][0]
    pswrd = password[i]
    letter_ocurrences = pswrd.count(letter)
    if letter_ocurrences >= low_limit and letter_ocurrences <= high_limit:
        sum += 1

print(sum)

# Part Two

sum = 0
for i in range(len(password)):
    low_limit = int(policy_limits[i].split("-")[0])
    high_limit = int(policy_limits[i].split("-")[1])
    letter = policy_char[i][0]
    pswrd = password[i]
    
    first_cond = pswrd[low_limit - 1] == letter
    second_cond = pswrd[high_limit - 1] == letter
    final_cond = first_cond + second_cond == 1
    if final_cond:
        sum += 1

print(sum)
