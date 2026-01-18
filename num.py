# Author: Bhavya Sharma
import math
import cmath
from fractions import Fraction

def analyze_number(n):
    info = {}

    # Basic properties
    info["value"] = n
    info["type"] = "integer" if isinstance(n, int) or n.is_integer() else "decimal"
    info["sign"] = "positive" if n > 0 else "negative" if n < 0 else "zero"
    info["absolute_value"] = abs(n)

    # Integer-specific properties
    if float(n).is_integer():
        n = int(n)
        info["even"] = (n % 2 == 0)
        info["odd"] = (n % 2 != 0)

        # Prime check
        if n > 1:
            info["prime"] = all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
        else:
            info["prime"] = False

        # Factors
        info["factors"] = [i for i in range(1, abs(n) + 1) if n % i == 0] if n != 0 else "infinite"

        # Perfect square / cube
        info["perfect_square"] = int(math.isqrt(abs(n)))**2 == abs(n)
        info["perfect_cube"] = round(abs(n) ** (1/3))**3 == abs(n)

        # Binary / Octal / Hex
        info["binary"] = bin(n)
        info["octal"] = oct(n)
        info["hexadecimal"] = hex(n)

    # Decimal / Rational info
    info["as_fraction"] = Fraction(n).limit_denominator()

    # Mathematical operations
    info["square"] = n ** 2
    info["cube"] = n ** 3
    info["square_root"] = math.sqrt(n) if n >= 0 else cmath.sqrt(n)
    info["log10"] = math.log10(n) if n > 0 else "undefined"
    info["natural_log"] = math.log(n) if n > 0 else "undefined"
    info["reciprocal"] = 1 / n if n != 0 else "undefined"

    # Trigonometry (radians)
    info["sin"] = math.sin(n)
    info["cos"] = math.cos(n)
    info["tan"] = math.tan(n)

    return info


# --------- RUN PROGRAM ---------
num = float(input("Enter any number: "))
result = analyze_number(num)

print("\n--- NUMBER ANALYSIS ---")
for key, value in result.items():
    print(f"{key}: {value}")
