def to_centimeters(inches):
    centimeters = inches * 2.54
    return centimeters


def to_inches(centimeters):
    inches = centimeters / 2.54
    return inches


def to_yards(feet):
    yards = feet / 3
    return yards


def to_feet(yards):
    feet = yards * 3
    return feet


def feet_to_miles(feet):
    miles = feet / 5280
    return miles


def miles_to_feet(miles):
    feet = miles * 5280
    return feet
