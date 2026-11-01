def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Brilliant', 'Nurhaimin',
location='UNS',
field='Industrial Engineering',
birthday='January 4, 2000')
print(user_profile)