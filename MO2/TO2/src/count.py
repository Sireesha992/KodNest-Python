limit = 10
target = 6
count = 0
total = 0
target_found = False
for i in range(1,limit+1):
    if i%3==0:
        count+=1
        total+=i
        if i == target:
            target_found = True
if target_found:
    found_status = "Yes"
else:
    found_status = "No"
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Target Found: {found_status}")