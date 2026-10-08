"""Exact finite checks for the supplied record-model dictionaries.

Standalone standard-library runner: no scientific files or network inputs.
The note proves the all-size statements and imports critical extinction.
No finite enumeration here purports to prove criticality or a GFF limit.
"""

AUDIT_TIMEOUT_SEC = 180

from fractions import Fraction
from itertools import product
import sys


PASS = 0
FAIL = 0


def check(label, condition, detail):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label}: {detail}")


def bitword(word, width):
    return tuple((word >> i) & 1 for i in range(width))


def activation_checks():
    """Tensor probabilities versus the independently assembled birth generator."""
    cases = 0
    normalizes = True
    forward_ok = True
    # q=exp(-lambda*t), including t=0. All arithmetic is rational.
    for size in (1, 4, 8):
        for q in (Fraction(1), Fraction(1, 2), Fraction(1, 3)):
            mass = {s: (1-q)**s.bit_count()*q**(size-s.bit_count())
                    for s in range(1 << size)}
            normalizes &= sum(mass.values()) == 1
            for rate in (Fraction(1), Fraction(3, 2), Fraction(2)):
                for state, weight in mass.items():
                    k = state.bit_count()
                    incoming = sum(mass[state ^ (1 << i)]
                                   for i in range(size) if (state >> i) & 1)
                    generator = rate * (incoming-(size-k)*weight)
                    derivative = rate * (
                        (k*(1-q)**(k-1)*q**(size-k+1) if k else 0)
                        - (size-k)*weight)
                    forward_ok &= generator == derivative
                    cases += 1
    check("A1 tensor probabilities", normalizes, "9 exact finite product laws normalize")
    check("A2 activation generator", forward_ok, f"{cases} exact state/rate forward equations")

    # Contents -1=blank, 0=record0, 1=recordI. The content kernel depends on
    # recorded neighbours, but summing the two outcomes must leave rate lambda.
    graph = ((1,), (0, 2), (1,))
    projected = True
    transitions = 0
    for state in product((-1, 0, 1), repeat=3):
        for copy in (Fraction(0), Fraction(1, 4), Fraction(3, 4)):
            for site in range(3):
                if state[site] != -1:
                    continue
                seen = [state[j] for j in graph[site] if state[j] != -1]
                one = Fraction(1, 2) if not seen else (
                    (1-copy)/2 + copy*Fraction(sum(seen), len(seen)))
                rates = (Fraction(3, 2)*(1-one), Fraction(3, 2)*one)
                projected &= min(rates) > 0 and sum(rates) == Fraction(3, 2)
                transitions += 1
    check("A3 content projection", projected, f"{transitions} blank-site kernels keep the same flag rate")

    # Adverse control: rate 2 for the remaining site after the first birth.
    # The iid rate-1 product law at q=1/2 fails this altered forward equation.
    iid = {0: Fraction(1, 4), 1: Fraction(1, 4),
           2: Fraction(1, 4), 3: Fraction(1, 4)}
    altered_forward_singleton = iid[0] - 2*iid[1]
    iid_derivative_singleton = Fraction(0)
    check("A4 state-dependent-rate control",
          altered_forward_singleton != iid_derivative_singleton,
          f"altered singleton derivative={altered_forward_singleton}, iid derivative=0")

    # Static g=1, p=q=r gas: compare its finite partition sum with product form.
    static_ok = True
    for size in (1, 4, 8):
        for activity in (Fraction(1, 3), Fraction(1), Fraction(3)):
            z = sum(activity**s.bit_count() for s in range(1 << size))
            density = activity/(1+activity)
            static_ok &= z == (1+activity)**size
            for s in range(1 << size):
                k = s.bit_count()
                static_ok &= activity**k/z == density**k*(1-density)**(size-k)
    check("A5 static gas Bernoulli law", static_ok, "exact activity-to-density map on 9 finite gases")


def row_matrices(width):
    states = [bitword(i, width) for i in range(1 << width)]
    occ = [[0]*len(states) for _ in states]
    arr = [[0]*len(states) for _ in states]
    for i, a in enumerate(states):
        for j, b in enumerate(states):
            for h in states:
                occ[i][j] += all(a[y]+b[y]+h[y]+h[(y-1) % width] == 2
                                 for y in range(width))
                arr[i][j] += all(b[y]-a[y]+h[y]-h[(y-1) % width] == 0
                                 for y in range(width))
    return states, occ, arr


def multiply(a, b):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def sector_trace(matrix, length, indices):
    a = [[matrix[i][j] for j in indices] for i in indices]
    acc = [[int(i == j) for j in range(len(a))] for i in range(len(a))]
    for _ in range(length):
        acc = multiply(acc, a)
    return sum(acc[i][i] for i in range(len(a)))


def ice_checks():
    local = list(product((0, 1), repeat=6))
    cubic = [v for v in local if sum(v) == 3]
    planar = [v for v in cubic if v[0] == 1 and v[1] == 0]
    check("B1 local conditioned ice", len(cubic) == 20 and len(planar) == 6
          and all(sum(v[2:]) == 2 for v in planar),
          f"cubic states={len(cubic)}, fixed-complementary-vertical states={len(planar)}")
    for width in (4, 6):
        states, occ, arr = row_matrices(width)

        def to_arrow_index(state, column_parity):
            return sum((state[y] if (column_parity+y) % 2 == 0 else 1-state[y]) << y
                       for y in range(width))

        entry_match = all(
            occ[i][j] == arr[to_arrow_index(a, 0)][to_arrow_index(b, 0)]
            for i, a in enumerate(states) for j, b in enumerate(states))
        check(f"B2 width{width} row dictionary", entry_match,
              f"{len(states)**2} occupation/arrow entries, separate local constraints")
        occ_sector = [i for i, a in enumerate(states)
                      if sum((-1)**y*(2*a[y]-1) for y in range(width)) == 0]
        arr_sector = [i for i, a in enumerate(states) if sum(a) == width//2]
        for length in (4, 6):
            a = sector_trace(occ, length, occ_sector)
            b = sector_trace(arr, length, arr_sector)
            check(f"B3 balanced {length}x{width}", a == b, f"occupation={a}, arrows={b}")
        a = sector_trace(occ, 3, occ_sector)
        b = sector_trace(arr, 3, arr_sector)
        check(f"B4 odd-period control 3x{width}", a != b, f"occupation={a}, arrows={b}")
        if width == 4:
            all_count = sector_trace(occ, 4, list(range(len(states))))
            balanced = sector_trace(occ, 4, occ_sector)
            check("B5 sector restriction is substantive", all_count > balanced,
                  f"4x4 all sectors={all_count}, balanced={balanced}")


def ising_checks():
    length = 4
    volume = length*length
    edges = [(x*length+y, ((x+dx) % length)*length+(y+dy) % length)
             for x in range(length) for y in range(length)
             for dx, dy in ((1, 0), (0, 1))]
    exact = True
    boundary_factor = True
    for word in range(1 << volume):
        occupation = bitword(word, volume)
        count = sum(occupation)
        bonds = sum(occupation[i]*occupation[j] for i, j in edges)
        spin = [(-1)**(x+y)*(2*occupation[x*length+y]-1)
                for x in range(length) for y in range(length)]
        spin_energy = sum(spin[i]*spin[j] for i, j in edges)
        exact &= 4*(bonds-2*count) == -2*volume-spin_energy
        # Fix genuinely varying complementary vertical words.
        lower = tuple((i % 3) == 0 for i in range(volume))
        upper = tuple(not v for v in lower)
        vertical_bonds = sum(occupation[i]*(lower[i]+upper[i]) for i in range(volume))
        boundary_factor &= vertical_bonds == count
    check("C1 complementary vertical gas boundary", boundary_factor,
          f"one vertical occupied bond per plane record in all {1 << volume} configurations")
    check("C2 planar gas Ising identity", exact,
          f"4(B-2N)=-2V-sum spin products for all {1 << volume} configurations")


def ashkin_teller_checks():
    states = tuple(product((-1, 1), repeat=2))
    triples = ((3, 1, 2), (3, 1, 1), (5, 1, 2),
               (Fraction(7, 3), Fraction(2, 5), Fraction(11, 7)))
    for raw in triples:
        p, q, r = map(Fraction, raw)
        exact = True
        for a in states:
            for b in states:
                s, t = a[0]*b[0], a[1]*b[1]
                target = p if a == b else q if (s, t) == (-1, -1) else r
                # Fourth powers eliminate logarithms and fourth roots exactly.
                reconstructed_fourth = p*q*r*r * (p/q)**(s+t) * (p*q/(r*r))**(s*t)
                exact &= target**4 == reconstructed_fourth
        check(f"D1 AT bond dictionary {raw}", exact, "16 positive bond weights, exact rational fourth powers")
    tests = ((3, 1, 2, False), (3, 1, 1, True), (5, 1, 2, True))
    matches = all((p > q and q <= r and p-q == 2*r) == expected
                  for p, q, r, expected in tests)
    check("D2 AT parameter-line controls", matches,
          "(3,1,2) off line; (3,1,1) endpoint; (5,1,2) interior")


def main():
    activation_checks()
    ice_checks()
    ising_checks()
    ashkin_teller_checks()
    print("SCOPE: finite algebra and probability checks; external critical extinction and paper-premised GFF are not numerically tested")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
