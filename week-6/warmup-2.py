def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

c_degrees = 0
f_degrees = celsius_to_fahrenheit(c_degrees)
print(f"{c_degrees:.1f}C equals {f_degrees:.1f}F.")

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

f_degree = 32
c_degree = fahrenheit_to_celsius(f_degree)
print(f"{f_degree:.1f}F equals {c_degree:.1f}")