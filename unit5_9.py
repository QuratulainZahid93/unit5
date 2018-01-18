current_users = ['aney', 'zain', 'mubashir', 'sanobar', 'kb']
new_users = ['sarah', 'zain', 'sabir', 'Kb', 'humza']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")

        current_users_lower = []
        for user in current_users:
            current_users_lower.append(user.lower())