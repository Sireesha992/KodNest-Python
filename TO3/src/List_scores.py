n = 5
scores = [28, 92, 61, 84, 87]
search_score = 92
print(f"Highest Score: {max (scores)}")
print(f"Lowest score: {min (scores)}")
print(f"Total score: {sum(scores)}")
if search_score in scores:
    print("Search Result: Found")
else:

    print("Search Result: Not Found")