login_data = {
    'username': 'john_doe',
    'password': 'password123',
    'passwordRevisionDate': '2023-01-01'
}

# Before deletion
print("Before deletion:", login_data)

# Delete 'passwordRevisionDate' from login_data
del login_data['passwordRevisionDate']

# After deletion
print("After deletion:", login_data)
