def min_to_hr(minutes, seconds):
    hours = minutes / 60 + seconds / 3600
    return hours

print("Hours:")
print(min_to_hr(62, 0))


def sec_to_hr(seconds):
    hours = seconds / 3600
    return hours

print(sec_to_hr(7000))