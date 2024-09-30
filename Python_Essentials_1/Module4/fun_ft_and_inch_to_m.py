def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(1, 1))
print(ft_and_inch_to_m(6, 0))

def ft_and_inch_to_m2(ft, inch = 0.0): # default
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m2(6))