def sort(width, height, length, mass):
    
    # Check heavy first (cheap operation)
    heavy = mass >= 20

    # Check bulky (short-circuit before multiplication if possible)
    if width >= 150 or height >= 150 or length >= 150:
        bulky = True
    else:
        bulky = width * height * length >= 1_000_000

    # Decision logic (ordered for fastest exit)
    if heavy and bulky:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
