## Combine lists + dicts + function:
# Write a function that takes a list of usernames and returns a dictionary with username → length of name.
def username_lengths(users):
    return {user: len(user) for user in users}
print(username_lengths(["Ashu", "vico", "mike"]))