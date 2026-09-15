"""Refuting pass, block 20 (supervisor seat, disjoint machinery from the runner's checks):
(R1) H1 on the exactly solvable two-site instance (Z/2Z, N = 2, two bonds, weight e^{2 beta s1.s2}): <s1.s2> = coth(2 beta) - 1/(2 beta) =: Lam;
     u(pi) = (1 - Lam)/3, M^2 = (1 + Lam)/2, E(pi) = 4; check the displayed lower bound and its simplified form at beta = 1/2, 1, 2, 5;
     the sum rule u(0) + u(pi) = N/3 exactly;
(R2) the plane: N^{-1} sum_{k != 0} 1/(beta E(k) + 4/(3N)) evaluated directly (floating point, exact cosines) for L = 2..64 and
     beta = 1/4, 1, 4, against the proved lower bound H_{L-1}/(pi^2 beta + 1/3); the implied bound 3/S on M^4 against the note's (3 pi^2 beta + 1)/H_{L-1};
(R3) the line: the same for L = 2..400 against m/(beta pi^2 + 2/3), m = floor(sqrt L), and 3/S_1 against (6 pi^2 beta + 4)/sqrt L;
     the first run included L = 1 and found the lower bound violated at beta = 1/4: at L = 1 the range {-L+1..L} = {0, 1} holds only n = 1,
     so the count 2m of the block fails there (finding folded: H2(e) and the line half of H3 are stated for L >= 2);
(R4) the sphere average of (s^1)^2 with the polar axis along e_1 (symbolic); Parseval on a random real field on a 6x6 torus (direct sums);
(R5) H_{L-1} >= log L for L = 2..10^4 (the dyadic bound of the note is the weaker, exact-checkable form)."""
import cmath
import math
import random
from fractions import Fraction

import sympy as sp

b = sp.symbols("beta", positive=True)
Lam = sp.coth(2 * b) - 1 / (2 * b)
u_pi = (1 - Lam) / 3
M2 = (1 + Lam) / 2
E = 4
N = 2
full = (2 * M2 / 3) ** 2 / (sp.sqrt(b * E) + sp.sqrt(b * E + 4 * M2 / (3 * N))) ** 2
simp = (M2 / 3) ** 2 / (b * E + sp.Rational(4, 3) / N)
ok1 = True
for bv in (sp.Rational(1, 2), 1, 2, 5):
    vals = [sp.N(x.subs(b, bv), 15) for x in (u_pi, full, simp, M2)]
    ok1 = ok1 and vals[0] >= vals[1] >= vals[2]
    print(f"R1 beta={bv}: u(pi)={vals[0]:.6f} >= full bound {vals[1]:.6f} >= simplified {vals[2]:.6f} (M^2={vals[3]:.4f}): {vals[0] >= vals[1] >= vals[2]}")
u_0 = (1 + Lam) / 3
print("R1 sum rule u(0) + u(pi) = N/3 exactly:", sp.simplify(u_0 + u_pi - sp.Rational(N, 3)) == 0, "; all four couplings consistent:", ok1)


def H(n):
    return sum(1.0 / j for j in range(1, n + 1))


ok2 = True
for beta in (0.25, 1.0, 4.0):
    for L in range(2, 65):
        Nn = 4 * L * L
        S = 0.0
        for n1 in range(-L + 1, L + 1):
            for n2 in range(-L + 1, L + 1):
                if (n1, n2) == (0, 0):
                    continue
                Ek = 2 * (1 - math.cos(math.pi * n1 / L)) + 2 * (1 - math.cos(math.pi * n2 / L))
                S += 1.0 / (beta * Ek + 4.0 / (3 * Nn))
        S /= Nn
        lower = H(L - 1) / (math.pi ** 2 * beta + 1.0 / 3)
        note_bound = (3 * math.pi ** 2 * beta + 1) / H(L - 1)
        ok2 = ok2 and S >= lower and 3.0 / S <= note_bound
        if L in (2, 8, 64) and beta == 1.0:
            print(f"R2 plane L={L}: S={S:.5f} >= {lower:.5f}; implied M^4 <= {3/S:.4f} <= note's {note_bound:.4f}")
print("R2 plane: direct sums dominate the proved lower bound, and the note's bound is the weaker one, for L = 2..64, beta = 1/4, 1, 4:", ok2)
ok3 = True
bad3 = []
for beta in (0.25, 1.0, 4.0):
    for L in range(1, 401):
        Nn = 2 * L
        S = 0.0
        for n in range(-L + 1, L + 1):
            if n == 0:
                continue
            Ek = 2 * (1 - math.cos(math.pi * n / L))
            S += 1.0 / (beta * Ek + 4.0 / (3 * Nn))
        S /= Nn
        m = math.isqrt(L)
        lower = m / (beta * math.pi ** 2 + 2.0 / 3)
        note_bound = (6 * math.pi ** 2 * beta + 4) / math.sqrt(L)
        if L >= 2:
            ok3 = ok3 and S >= lower and 3.0 / S <= note_bound
        elif not (S >= lower and 3.0 / S <= note_bound):
            bad3.append((L, beta))
        if L in (1, 16, 400) and beta == 1.0:
            print(f"R3 line L={L}: S={S:.5f} >= {lower:.5f}; implied M^4 <= {3/S:.4f} <= note's {note_bound:.4f}")
print("R3 line: direct sums dominate the proved lower bound, and the note's bound is the weaker one, for L = 2..400, beta = 1/4, 1, 4:", ok3, "; L = 1 violations (the count 2m fails there):", bad3)
th, ph = sp.symbols("theta phi", real=True)
avg = sp.integrate(sp.integrate(sp.cos(th) ** 2 * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi)) / (4 * sp.pi)
random.seed(20)
Lt = 6
field = {(x, y): random.uniform(-1, 1) for x in range(Lt) for y in range(Lt)}
tot = 0.0
for n1 in range(Lt):
    for n2 in range(Lt):
        hat = sum(cmath.exp(2j * math.pi * (n1 * x + n2 * y) / Lt) * v for (x, y), v in field.items()) / math.sqrt(Lt * Lt)
        tot += abs(hat) ** 2
print("R4 sphere average with the polar axis along e_1:", avg, "; Parseval residue on a random 6x6 field:", f"{abs(tot - sum(v * v for v in field.values())):.1e}")
print("R5 H_(L-1) >= log L for L = 2..10^4:", all(H(L - 1) >= math.log(L) for L in range(2, 10001)))
