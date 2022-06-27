import random


def unique_code_generator(instance):
    not_unique = True
    while not_unique:
        code = random.randint(100000, 999999)
        klass = instance.__class__
        qs_exists = klass.objects.filter(code=code).exists()
        if not qs_exists:
            not_unique = False
    return str(code)
