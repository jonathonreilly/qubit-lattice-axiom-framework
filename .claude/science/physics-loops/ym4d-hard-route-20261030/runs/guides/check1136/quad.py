"""GUIDE: quadrature of E chi_d under the commutator density w = (pi - th)/(2 sin th)."""
import math
n = 400000
for d in (2, 3, 4, 5, 6):
    s = 0.0
    for i in range(n):
        th = math.pi * (i + 0.5) / n
        s += (math.pi - th) / (2 * math.sin(th)) * (math.sin(d * th) / math.sin(th)) * (2 / math.pi) * math.sin(th) ** 2 * (math.pi / n)
    print(f"d={d}: quadrature E chi_d = {s:.6f} vs 1/d = {1/d:.6f}")
