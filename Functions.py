def enter(n):
    try:
        return int(n)
    except ValueError:
        return False


def enter_str(n):
    if n != 'y' or n != 'n':
        return False
    else:
        return True
