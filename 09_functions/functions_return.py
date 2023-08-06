def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy New Year!")
    print("Let's hope that this year will be better than the previous one.")


happy_new_year()
happy_new_year(False)


def strange_list_function(n):
    strange_list = []
    for i in range(0, n):
        strange_list.insert(0, i)
    return strange_list


print(strange_list_function(5))


def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


def is_prime(num):
    for i in range(2, int(1 + num**0.5)):
        if num % i == 0:
            return False
    return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
