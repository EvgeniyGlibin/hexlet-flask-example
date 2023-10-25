def validate(user):
    errors = {}
    if not user.get('name'):
        errors['name'] = "Can't be blank"
    if not user.get('email'):
        errors['email'] = "Can't be blank"
    if not user.get('city'):
        errors['city'] = "Can't be blank"
    return errors