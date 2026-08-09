number_count = 6
positive_count = 0
negative_count = 0
zero_count = 0
total = 0
for i in range(number_count):
    number = [5, 10 ,-4, 0, 7, -3]
    total = total + number[i]
    if number[i] > 0:
       positive_count+=1
    elif number[i] < 0:
        negative_count+=1
    else:
        zero_count+=1
print(f"Positive Count: {positive_count}")
print(f"Negative Count: {negative_count}")
print(f"Zero Count: {zero_count}")
print(f"Total: {total}")
    