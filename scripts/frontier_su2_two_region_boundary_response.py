#!/usr/bin/env python3
"""Exact supplemental controls for the supplied finite SU(2) soft-kernel model.

General proofs are in the paired note. These finite examples do not establish
all-volume comparison, all odd block lengths, or a physical mass gap.
The cumulant and path controls adapt the original FULL_PROOF_CHECK examples;
the shared-edge control integrates monomials on S^3 independently of the
radial-Hessian formula. No sampling, fitted value or numerical integration.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import permutations, product
from math import factorial, prod
from pathlib import Path
import hashlib

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = (
    "docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md",
)


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    print("PASS:", name)


def partitions(xs):
    if not xs:
        yield []
        return
    a, *tail = xs
    for p in partitions(tail):
        yield [(a,)] + p
        for i in range(len(p)):
            yield p[:i] + [(a,) + p[i]] + p[i + 1:]


def mean(vals, probabilities):
    return sum(v * p for v, p in zip(vals, probabilities))


def cumulant(vectors, probabilities):
    ans = Q(0)
    for p in partitions(list(range(len(vectors)))):
        term = Q((-1) ** (len(p) - 1) * factorial(len(p) - 1))
        for block in p:
            term *= mean([prod(vectors[i][u] for i in block)
                          for u in range(len(probabilities))], probabilities)
        ans += term
    return ans


def cumulant_controls():
    weights = [[Q((u + 1) * (x + 2) + (u * u + 3 * x) % 7 + 1)
                for u in range(6)] for x in range(3)]
    total = sum(map(sum, weights))
    p = [sum(row) / total for row in weights]
    pi = [[w / sum(row) for w in row] for row in weights]
    mu = [sum(weights[x][u] for x in range(3)) / total for u in range(6)]
    ys = [[Q(u - 2) for u in range(6)], [Q(u * u % 7 - 3) for u in range(6)],
          [Q((-1) ** u * (u + 1)) for u in range(6)],
          [Q(3 * u % 5 - 2) for u in range(6)]]
    for n in (2, 3, 4):
        groups = {}
        for partition in partitions(list(range(n))):
            vectors = [[cumulant([ys[i] for i in b], pp) for pp in pi]
                       for b in partition]
            key = tuple(sorted(map(len, partition), reverse=True))
            groups[key] = groups.get(key, Q(0)) + cumulant(vectors, p)
        discrepancy = cumulant(ys[:n], mu) - sum(groups.values())
        check(f"total cumulance order {n}; all partition types exercised",
              discrepancy == 0 and all(v != 0 for v in groups.values()))
    # Repeated boundary insertions in the fourth derivative are labelled,
    # not collapsed into a single random variable before partitioning.
    ys[3] = ys[2]
    rhs = sum(cumulant([[cumulant([ys[i] for i in b], pp) for pp in pi]
                       for b in partition], p)
              for partition in partitions([0, 1, 2, 3]))
    check("fourth cumulance with repeated insertion", rhs == cumulant(ys, mu))


def sphere_moment(exponents):
    """Normalized S^3 monomial integral from the Dirichlet(1/2) moments."""
    if any(k % 2 for k in exponents):
        return Q(0)
    n = sum(exponents) // 2
    numerator = prod(prod(range(1, k, 2)) for k in exponents)
    return Q(numerator, prod(range(4, 4 + 2 * n, 2)))


def polynomial_product(a, b):
    out = {}
    for e, v in a.items():
        for f, w in b.items():
            g = tuple(x + y for x, y in zip(e, f))
            out[g] = out.get(g, Q(0)) + v * w
    return out


def linear(coefficients):
    return {tuple(int(i == j) for i in range(4)): Q(coefficients[j])
            for j in range(4)}


def integrate(polynomial):
    return sum(c * sphere_moment(e) for e, c in polynomial.items())


def series_quotient(a, b, degree):
    out = []
    for n in range(degree + 1):
        out.append((a[n] - sum(b[k] * out[n - k] for k in range(1, n + 1))) / b[0])
    return out


def shared_edge_controls():
    check("Haar fixed-remainder shared edge retains 1/4",
          sphere_moment((2, 0, 0, 0)) == Q(1, 4))
    # A,B are unit quaternions, with opposite orientations on the shared V.
    examples = [((Q(1, 4),) * 4, (0, 1, 0, 0), (0, 0, 1, 0)),
                ((Q(1, 2), 0, 0, 0), (1, 0, 0, 0), (1, 0, 0, 0)),
                ((Q(1, 4),) * 4, (0, 1, 0, 0), (0, -1, 0, 0))]
    for index, (m, aa, bb) in enumerate(examples):
        r2 = sum(x * x for x in m)
        p = linear((aa[0], *(-x for x in aa[1:])))
        q = linear(bb)
        pq = polynomial_product(p, q)
        tilt = linear(m)
        power = {(0, 0, 0, 0): Q(1)}
        denominator, raw = [], []
        for n in range(9):
            denominator.append(integrate(power) / factorial(n))
            raw.append(integrate(polynomial_product(power, pq)) / factorial(n))
            power = polynomial_product(power, tilt)
        direct = series_quotient(raw, denominator, 6)
        # Prediction from the note, evaluated by its independent radial series.
        z = [Q(0)] * 9
        for n in range(5):
            z[2 * n] = r2 ** n / (4 ** n * factorial(n) * factorial(n + 1))
        transverse = series_quotient([(n + 2) * z[n + 2] / r2
                                     for n in range(7)], z, 6)
        ab = aa[0] * bb[0] - sum(x * y for x, y in zip(aa[1:], bb[1:]))
        ma = m[0] * aa[0] - sum(x * y for x, y in zip(m[1:], aa[1:]))
        mb = sum(x * y for x, y in zip(m, bb))
        predicted = [transverse[n] * ab +
                     (int(n == 0) - 4 * transverse[n]) * ma * mb / r2
                     for n in range(7)]
        check(f"shared-edge exact series through degree six, orientation case {index}",
              denominator == z and direct == predicted)


def axial(root, destination, order):
    current = list(root)
    edges = []
    for d in order:
        while current[d] != destination[d]:
            sign = 1 if destination[d] > current[d] else -1
            base = current.copy()
            if sign < 0:
                base[d] -= 1
            edges.append((tuple(base), d))
            current[d] += sign
    return edges


def geometry_controls():
    orders = list(permutations(range(4)))
    for length in (3, 5):
        half = (length - 1) // 2
        period = 3 * length
        supports = []
        repeated = 0
        max_radius = Q(0)
        for d in range(4):
            root = (0, 0, 0, 0)
            target = tuple(length if k == d else 0 for k in range(4))
            support = set()
            for y in product(range(-half, half + 1), repeat=4):
                yy = tuple(y[k] + (length if k == d else 0) for k in range(4))
                for order in orders:
                    path = (axial(root, y, order) + axial(y, yy, (d,)) +
                            list(reversed(axial(target, yy, order))))
                    repeated += len(set(path)) < len(path)
                    support.update(path)
            supports.append(support)
            for pos, edge in support:
                mid = [pos[k] + (Q(1, 2) if k == edge else 0) for k in range(4)]
                dist = sum(min(abs(mid[k] - (Q(length, 2) if k == d else 0)) % period,
                               period - abs(mid[k] - (Q(length, 2) if k == d else 0)) % period)
                           for k in range(4))
                max_radius = max(max_radius, dist)
        incidence = Counter()
        for block in product(range(3), repeat=4):
            for support in supports:
                for pos, edge in support:
                    incidence[(tuple((pos[k] + length * block[k]) % period
                                     for k in range(4)), edge)] += 1
        bound = (8 * length - 7) * length ** 3
        check(f"block length {length}: support, incidence, radius, repeated-edge control",
              all(len(s) <= bound for s in supports) and
              max(incidence.values()) <= 8 and max_radius <= 5 * length and repeated > 0)
        print(f"  supports={[len(s) for s in supports]} incidence={max(incidence.values())} "
              f"radius={max_radius} repeated_paths={repeated}")


def main():
    source = Path(__file__).resolve().parents[1] / AUDIT_INPUT_PATHS[0]
    print("Source SHA256:", hashlib.sha256(source.read_bytes()).hexdigest())
    print("Exact finite controls only; general proof and physical-scale obligation are in the note.")
    cumulant_controls()
    shared_edge_controls()
    geometry_controls()
    print("TOTAL: PASS=10 FAIL=0")


if __name__ == "__main__":
    main()
