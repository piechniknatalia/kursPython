import fractions

def skracanie(frac):
    if frac[0] == 0:
        return [0, 0]
    else:
        return [frac[0]/fractions.gcd(frac[0], frac[1]), frac[1]/fractions.gcd(frac[0], frac[1])]

print(skracanie([12, 9]))