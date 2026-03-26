def sort(width, height, length, mass):
    heavy = mass >= 20

    if width >= 150 or height >= 150 or length >= 150:
        bulky = True
    else:
        bulky = width * height * length >= 1_000_000

    if heavy and bulky:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
