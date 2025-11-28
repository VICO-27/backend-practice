## Loop through scores
# Print “Passed” if score ≥ 80, else “Failed”
from dictionaries import *
for user, score in scores.items():
    if score >= 80:
        print(f"{user} passed")
    else:
        print(f"{user} failed")